from typing import Callable, Tuple

from prometheus_client import Histogram, Summary, Counter
from starlette.requests import Request
from starlette.responses import Response


class Info:
    def __init__(
        self,
        request: Request,
        response: Response or None,
        method: str,
        modified_handler: str,
        modified_status: str,
        modified_duration: float,
    ):
        """Creates Info object that is used for instrumentation functions.

        This is the only argument that is passed to the instrumentation functions.

        Args:
            request: Python Requests request object.
            response Python Requests response object.
            method: Unmodified method of the request.
            modified_handler: Handler representation after processing by 
                instrumentator. For example grouped to `none` if not templated.
            modified_status: Status code representation after processing by
                instrumentator. For example grouping into `2xx`, `3xx` and so on.
            modified_duration: Latency representation after processing by 
                instrumentator. For example rounding of decimals. Seconds.
        """

        self.request = request
        self.response = response
        self.method = method
        self.modified_handler = modified_handler
        self.modified_status = modified_status
        self.modified_duration = modified_duration


def _build_label_attribute_names(
    should_include_handler: bool,
    should_include_method: bool,
    should_include_status: bool,
) -> Tuple[list, list]:
    """Builds up tuple with to be used label and attribute names.

    Args:
        should_include_handler: Should the `handler` label be part of the metric?
        should_include_method: Should the `method` label be part of the metric?
        should_include_status: Should the `status` label be part of the metric?

    Returns:
        Tuple with two list elements.

        First element: List with all labels to be used.
        Second element: List with all attribute names to be used from the 
            `Info` object. Done like this to enable dynamic on / off of labels.
    """

    label_names = []
    info_attribute_names = []

    if should_include_handler:
        label_names.append("handler")
        info_attribute_names.append("modified_handler")

    if should_include_method:
        label_names.append("method")
        info_attribute_names.append("method")

    if should_include_status:
        label_names.append("status")
        info_attribute_names.append("modified_status")

    return label_names, info_attribute_names


# Metrics ======================================================================


def latency(
    metric_name: str = "http_request_duration_seconds",
    metric_doc: str = "Duration of HTTP requests in seconds",
    should_include_handler: bool = True,
    should_include_method: bool = True,
    should_include_status: bool = True,
    buckets: tuple = Histogram.DEFAULT_BUCKETS,
) -> Callable[[Info], None]:
    """Default metric for the Prometheus FastAPI Instrumentator.

    Args:
        metric_name: Name of the metric to be created. Must be unique.
        metric_doc: Documentation of the metric.
        should_include_handler: Should the `handler` label be part of the metric?
        should_include_method: Should the `method` label be part of the metric?
        should_include_status: Should the `status` label be part of the metric?
        buckets: Buckets for the histogram. Defaults to Prometheus default.

    Returns:
        Function that takes a single parameter `Info`.
    """

    if buckets[-1] != float("inf"):
        buckets = buckets + (float("inf"),)

    label_names, info_attribute_names = _build_label_attribute_names(
        should_include_handler, should_include_method, should_include_status
    )

    if label_names:
        METRIC = Histogram(
            metric_name, metric_doc, labelnames=label_names, buckets=buckets
        )
    else:
        METRIC = Histogram(metric_name, metric_doc, buckets=buckets)

    def instrumentation(info: Info) -> None:
        if label_names:
            label_values = []
            for attribute_name in info_attribute_names:
                label_values.append(getattr(info, attribute_name))
            METRIC.labels(*label_values).observe(info.modified_duration)
        else:
            METRIC.observe(info.modified_duration)

    return instrumentation


def request_size(
    metric_name: str = "http_request_size_bytes",
    metric_doc: str = "Content bytes of requests.",
    should_include_handler: bool = True,
    should_include_method: bool = True,
    should_include_status: bool = True,
) -> Callable[[Info], None]:
    """Record the content length of incoming requests.

    Requests / Responses with missing `Content-Length` will be skipped.

    Args:
        metric_name: Name of the metric to be created. Must be unique.
        metric_doc: Documentation of the metric.
        should_include_handler: Should the `handler` label be part of the metric?
        should_include_method: Should the `method` label be part of the metric?
        should_include_status: Should the `status` label be part of the metric?

    Returns:
        Function that takes a single parameter `Info`.
    """

    label_names, info_attribute_names = _build_label_attribute_names(
        should_include_handler, should_include_method, should_include_status
    )

    if label_names:
        METRIC = Summary(metric_name, metric_doc, labelnames=label_names)
    else:
        METRIC = Summary(metric_name, metric_doc)

    def instrumentation(info: Info) -> None:
        content_length = info.request.headers.get("Content-Length", None)
        if content_length is not None:
            if label_names:
                label_values = []
                for attribute_name in info_attribute_names:
                    label_values.append(getattr(info, attribute_name))
                METRIC.labels(*label_values).observe(int(content_length))
            else:
                METRIC.observe(int(content_length))

    return instrumentation


def response_size(
    metric_name: str = "http_response_size_bytes",
    metric_doc: str = "Content bytes of responses.",
    should_include_handler: bool = True,
    should_include_method: bool = True,
    should_include_status: bool = True,
) -> Callable[[Info], None]:
    """Record the content length of outgoing responses.

    Responses with missing `Content-Length` will be skipped.

    Args:
        metric_name: Name of the metric to be created. Must be unique.
        metric_doc: Documentation of the metric.
        should_include_handler: Should the `handler` label be part of the metric?
        should_include_method: Should the `method` label be part of the metric?
        should_include_status: Should the `status` label be part of the metric?

    Returns:
        Function that takes a single parameter `Info`.
    """

    label_names, info_attribute_names = _build_label_attribute_names(
        should_include_handler, should_include_method, should_include_status
    )

    if label_names:
        METRIC = Summary(metric_name, metric_doc, labelnames=label_names)
    else:
        METRIC = Summary(metric_name, metric_doc)

    def instrumentation(info: Info) -> None:
        content_length = info.response.headers.get("Content-Length", None)
        if content_length is not None:
            if label_names:
                label_values = []
                for attribute_name in info_attribute_names:
                    label_values.append(getattr(info, attribute_name))
                METRIC.labels(*label_values).observe(int(content_length))
            else:
                METRIC.observe(int(content_length))

    return instrumentation


def combined_size(
    metric_name: str = "http_combined_size_bytes",
    metric_doc: str = "Content bytes of requests and responses.",
    should_include_handler: bool = True,
    should_include_method: bool = True,
    should_include_status: bool = True,
) -> Callable[[Info], None]:
    """Record the combined content length of requests and responses.

    Requests / Responses with missing `Content-Length` will be skipped.

    Args:
        metric_name: Name of the metric to be created. Must be unique.
        metric_doc: Documentation of the metric.
        should_include_handler: Should the `handler` label be part of the metric?
        should_include_method: Should the `method` label be part of the metric?
        should_include_status: Should the `status` label be part of the metric?

    Returns:
        Function that takes a single parameter `Info`.
    """

    label_names, info_attribute_names = _build_label_attribute_names(
        should_include_handler, should_include_method, should_include_status
    )

    if label_names:
        METRIC = Summary(metric_name, metric_doc, labelnames=label_names)
    else:
        METRIC = Summary(metric_name, metric_doc)

    def instrumentation(info: Info) -> None:
        request_cl = info.request.headers.get("Content-Length", None)
        response_cl = info.response.headers.get("Content-Length", None)

        if request_cl and response_cl:
            content_length = int(request_cl) + int(response_cl)
        elif request_cl:
            content_length = int(request_cl)
        elif response_cl:
            content_length = int(response_cl)
        else:
            content_length = None

        if content_length is not None:
            if label_names:
                label_values = []
                for attribute_name in info_attribute_names:
                    label_values.append(getattr(info, attribute_name))
                METRIC.labels(*label_values).observe(int(content_length))
            else:
                METRIC.observe(int(content_length))

    return instrumentation


def full(
    latency_highr_buckets: tuple = (
        .01,
        .025,
        .05,
        .075,
        .1,
        .25,
        .5,
        .75,
        1,
        1.5,
        2,
        2.5,
        3,
        3.5,
        4,
        4.5,
        5,
        7.5,
        10.,
    ),
    latency_lowr_buckets: tuple = (0.1, 0.5, 1),
) -> Callable[[Info], None]:
    """Contains multiple metrics to cover multiple things.

    Combines several metrics into a single function. Also more efficient than 
    multiple separate instrumentation functions that do more or less the same.
    
    You get the following:

    * `http_requests_total` (no labels): Total number of requests.
    * `http_in_bytes_total` (no labels): Total number of incoming content 
        length bytes.
    * `http_out_bytes_total` (no labels): Total number of outgoing content 
        length bytes.
    * `http_highr_request_duration_seconds` (no labels): High number of buckets 
        leading to more accurate calculation of percentiles.
    * `http_lowr_request_duration_seconds` (`handler`, `status`, `method`): 
        Kepp the bucket count very low. Only put in SLIs.

    Args:
        latency_highr_buckets: Buckets tuple for high res histogram. Can be 
            large because no labels are used.
        latency_lowr_buckets: Buckets tuple for low res histogram. Should be 
            very small as all possible labels are included.

    Returns:
        Function that takes a single parameter `Info`.
    """

    if latency_highr_buckets[-1] != float("inf"):
        latency_highr_buckets = latency_highr_buckets + (float("inf"),)

    if latency_lowr_buckets[-1] != float("inf"):
        latency_lowr_buckets = latency_lowr_buckets + (float("inf"),)

    TOTAL = Counter(
        "http_requests_total", "Total number of requests with no API specific labels."
    )

    IN_SIZE = Counter("http_in_bytes_total", "Content length of incoming requests.")
    OUT_SIZE = Counter("http_out_bytes_total", "Content length of incoming requests.")

    LATENCY_HIGHR = Histogram(
        "http_highr_request_duration_seconds",
        "Latency with many buckets but no API specific labels.",
        buckets=latency_highr_buckets,
    )

    LATENCY_LOWR = Histogram(
        "http_lowr_request_duration_seconds",
        "Latency with only few buckets.",
        buckets=latency_lowr_buckets,
        labelnames=("method", "status", "handler"),
    )

    def instrumentation(info: Info) -> None:
        TOTAL.inc()
        IN_SIZE.inc(int(info.request.headers.get("Content-Length", 0)))
        OUT_SIZE.inc(int(info.response.headers.get("Content-Length", 0)))
        LATENCY_HIGHR.observe(info.modified_duration)
        LATENCY_LOWR.labels(
            info.method, info.modified_status, info.modified_handler
        ).observe(info.modified_duration)

    return instrumentation