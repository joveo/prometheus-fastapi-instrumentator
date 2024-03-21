# Changelog

## [6.0.0](https://github.com/joveo/prometheus-fastapi-instrumentator/compare/v5.9.1...v6.0.0) (2024-03-21)


### ⚠ BREAKING CHANGES

* Removed support for Python 3.6 and overall cleanup
* **dev:** Switch from underscores to dashes for function names

### Features

* Add FastAPI tags support to `expose` method ([e1c0867](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e1c08679a3b1d745becd73394f06f756bcba3904))
* Add kwargs passthrough to FastAPI annotation ([f3ace89](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/f3ace895df3325eae0149765e60577b226e34ce3))
* add optional in progress metric ([e62576e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e62576e3640be0b677334537d27bc267ab0e91cf))
* Add py.typed for enhanced typing annotations ([#37](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/37)) ([0c67d1b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/0c67d1b8f51348979c00fd00d9457d3dd238df87))
* **ci:** Add `dependabot.yml` ([a6d6406](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/a6d640613a89972df4de7fe8dde06bf1457f93b8))
* **metrics:** Add `requests` metric closure ([4933e02](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/4933e02cf350910f5c1706e845ef9728f5349ebd))


### Bug Fixes

* **deps:** regression too strict version requirements [#136](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/136) ([36bc045](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/36bc045c5eb247fa7a83c25cc161f95b5d4b314d))
* **expose:** Duplicate mime type charset ([5cf109e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/5cf109e87c6a23ac5c1a271bc5b039d5ec84c8d0))
* fastapi version in 'pyproject.toml' ([eb13f6a](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/eb13f6ab346a304536e77d67fb886cccaa4d7813))
* Incorrect version constraint ([7ed3ab8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/7ed3ab8657e75094488622c0327d6254b75d8ca4))
* Missing coverage report creation ([5fca320](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/5fca320c09bed5b82855ae82a2b34888387ced17))
* **pdoc3:** Fix docstring args styleThe previous style seems to be incompitable with pdoc3. ([dc1071b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/dc1071bafc05c412885851fcb4a33cf70700f81c))
* Remove print statement from middleware ([#157](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/157)) ([f89792b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/f89792b63d286e2ffd9241dc0b04c927f1102d07))
* Remove trailing whitespace ([bb7f7c1](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/bb7f7c1bca7e641914aed63f2ad7fafaab450b94))


### Refactor

* **dev:** Switch from underscores to dashes for function names ([1dc0bb3](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1dc0bb331ff2484931030fe802d0ee19a84e13d4))
* Improve coding style ([#155](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/155)) ([623d83b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/623d83b86278d2627084b9fe9547f1af07531042))
* Improve type hinting and docstrings ([00c30d5](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/00c30d5570cdb2489fcf3162aca46b32f73a5729))
* remove support for python 3.6 and clean ([363d353](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/363d3534b78cafe50d288901890650d95a64e109))
* replace middleware implementation ([a9e68e3](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/a9e68e3fcaa6d3f669fe5f73607c483a53b391d2))
* resolve mypy finding ([1d898ee](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1d898ee5aa4105a9d0398fb8345cf13ce82e6ce2))


### Tests

* Add multiproc test to `run.sh` ([2d108df](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/2d108df00322c6dc7f2996744b4805d5b871421d))
* Add Pytest helping and configuration ([6ceba27](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/6ceba270c5e6f6b690b1266cc4b474926a8a6811))
* Fix failures due to changes in httpx ([1726297](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/172629796b11f35a7929a53c5ad9f2fa92abf7fe))
* Replace deprecated httpx parameter ([09aa996](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/09aa996955b3a9a2e656cc5c5b5a8162f74f74a1))


### Docs

* Add `DEVELOPMENT.md` ([9844cb3](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/9844cb3df8dbb45500091ead84614e3bb17531e7))
* Add CodeQL badge to `README.md` ([522a34e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/522a34e9573399aed84d333db20768edec408cfe))
* add comment regarding questions and ideas ([3caa7cf](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/3caa7cf25057ba906d6f3d3e039eb3f694855e5f))
* add disclaimer to README ([d8025f8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/d8025f894a6beb208b2dcd463bea08a0629251fd))
* Add missing colon to README ([#33](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/33)) ([faef24c](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/faef24c5aa4794cf1564ba871b15b736de303a86))
* Add missing docstring ([e48b9d8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e48b9d8e041fcc784a822cd697fae785a9bc4815))
* Add missing license and copyright header ([d91889f](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/d91889f0c6f5017fbfb5927e0ccfc0d552fa03e8))
* Adjust changelog formatting ([b8b7b3e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/b8b7b3ea2319947d8d5f9b8fb10c559267838516))
* **changelog:** add contribution info ([1032887](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1032887d54aaed21064e13222242fcd812ef2481))
* Fix small typo in readme ([#154](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/154)) ([a569d4e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/a569d4e58147a707c43e0fb698457c7ec7e13150))
* fix typo in badge link ([1d5c26a](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1d5c26ac446952ee4280cf595061c84ace4dfe26))
* Improve example in README on how to instrument app ([#168](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/168)) ([dc36aac](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/dc36aac1a530faa3970b19c1c68be4ee18c7c34b))
* Move docs-internal to docs/devel and adjust contributing ([1b446ca](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1b446ca3283514dcfbdaf9a1c5aa0f3a031ace45))
* Remove duplicate text from `README.md` [skip ci] ([7a1fa3c](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/7a1fa3c0c9b47b3d96024b22ac61480a283ecef2))
* Remove obsolete DEVELOPMENT.md ([1c18ff7](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1c18ff72df97892680c9da7c0193997c6795dc83))
* Small improvements ([8447835](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/84478351e7495710e14bbff578f903b1fb656dad))
* Switch from `pip freeze` to `poetry export` ([c21ab66](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/c21ab66ddc5bf12ddbe2acfb9b7d7cd0e047b856))
* Switch license from MIT to ISC ([1b0294a](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1b0294ac03b3369cae9b6cc675b9c94e1a4c0d76))
* Update and improve documentation ([f47d9f3](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/f47d9f3546c898e5a113d791bbe6a94dac100f00))
* Update pdoc3 docs ([7c2ae72](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/7c2ae72de1291e4828cb2aa1e018af5d31e80eac))
* update readme and bump version ([ae4e510](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/ae4e510b40b18806f4c0bd20bf07785f25d1d82d))


### Build

* Add dev dependencies `mypy` and `devtools` ([f58e62e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/f58e62eb033496ffb9257f1b132407f3aeb1864b))
* Bump to `5.7.0` ([99bd4b8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/99bd4b8d9125d73173c0d08ffdd8a055c3fb7083))
* Bump version ([46ca94e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/46ca94e90e9c4162efab4866d8989f185825aab9))
* **deps-dev:** bump devtools from 0.8.0 to 0.9.0 ([#172](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/172)) ([24bb060](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/24bb060a44b82b3b8d621d01af66dbd39773f2c7))
* **deps-dev:** bump flake8 from 4.0.1 to 5.0.4 ([#179](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/179)) ([8f72053](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/8f7205320ed648ef07fa21d7f699cf06cef3d4eb))
* **deps-dev:** bump mypy from 0.812 to 0.950 ([#131](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/131)) ([334d774](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/334d774a3d9e67c4474ed85c051ff868d29c76c8))
* **deps-dev:** bump mypy from 0.950 to 0.971 ([#174](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/174)) ([60e324f](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/60e324fb24f262f01f3d36be38c4e5e705523425))
* **deps:** bump codecov/codecov-action from 1 to 3 ([#122](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/122)) ([367da31](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/367da31b6a8d992d46224915b68fd6b508b821d3))
* **deps:** bump conventional-changelog-conventionalcommits in /node ([#145](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/145)) ([42ce6ca](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/42ce6cab9fb92982374ebc3174671ccdd6f1bee9))
* **deps:** bump pydantic from 1.7.3 to 1.7.4 ([17c0136](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/17c01360bd3a84d058c31cf86c46346cc549fcbd))
* **deps:** bump semver-regex from 3.1.3 to 3.1.4 in /node ([#147](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/147)) ([ce0b9cf](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/ce0b9cf2c7a44a6af04af769e3eb010d1994a8db))
* Manually update development dependencies ([c672942](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/c67294290a502fcb6d21882cec438e8c2e6947a6))
* Reliscense from MIT to Apache-2.0 ([d1d9848](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/d1d98480a7f9798cdd284e787cb8dd7c76886c16))
* Replace Makefile with Bash script ([2de6bd2](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/2de6bd2543357c67a7c2b813a1d079f84a79bfaf))
* Replace workflow files ([492000b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/492000b66508562135a78118b034cedc6973978f))
* Run `poetry update` ([063cacf](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/063cacfb10ec087fa649a687eb1e4126c8d3198c))
* Run Updating dependencies ([45e153e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/45e153e203e2863bd16421417111bc9c467208cf))
* Update dependencies with Updating dependencies ([d280ad5](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/d280ad5f55ffb41b9b21ea542e11ae834e627394))


### CI/CD

* Add .tool-versions ([255ba97](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/255ba97ee3dfbdada5fe300362b2725c075da0f8))
* Add codecov.yaml ([008ef61](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/008ef6136eba8d133a69de6f15ff14c39966fa2f))
* Add CodeQL workflow ([ac57bd0](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/ac57bd05edd611570ccf111bfc137f8160611258))
* Add explicit codecov token ([b264184](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/b264184cea3bfdb318fb007ed0972814a41014eb))
* Adjust commitlint to allow more subject case types ([8b630aa](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/8b630aa2734696effe78e95ab638b08fb594c908))
* Apply automatic changes [skip ci] ([02e807b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/02e807b76cd2692cf543e207fd07f926a69046d6))
* Apply automatic changes [skip ci] ([649ae2e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/649ae2e30cc2b1354421af362bd6069da2d404c1))
* Apply automatic changes [skip ci] ([45d0ba1](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/45d0ba1d03c565f2caca807b7df813e434c90ec8))
* Apply automatic changes [skip ci] ([3cdd94c](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/3cdd94c7b6e1158746a48af2a46ba08cd28273a0))
* Apply automatic changes [skip ci] ([bbb606b](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/bbb606becb79658f5bd99c5e9c860a88b5929ca1))
* change auto commit msgs ([0a199fe](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/0a199fe70103cd30c7554ebbf3d2425721f448b0))
* Correct default branch name ([5f141c5](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/5f141c59cc1b34b4cdbb2a77ba0edfc6c757356e))
* fix coverage report generation ([1ef3f43](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1ef3f430993a1aa1bbd271fe4e56a45a6823cde1))
* Improve and update scripts ([e1d9982](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e1d998213b811c20f09e9c717efd2a97165b7939))
* improve workflows ([97c68f8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/97c68f8e0e14076869eac9a106ff949f57d0f992))
* Move to Release Please and refactor overall CI approach ([9977665](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/99776659515910a7c1369bcc7db916d440590ee7))
* Pin poetry version and improve caching configuration ([6337459](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/6337459156a9cd87d868953e6c6c8dabea064eb1))
* Remove flake8 ignore W503 ([6eab3b8](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/6eab3b87fac913cf36b0266255304a917dec7b4f))
* remove poetry run from docs workflow ([219c6d2](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/219c6d2c3a18964b335da9f468b40bcd7b5ec06d))
* remove requirements.txt ([1bef98d](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/1bef98d746156a921be0406f7f08f8b5810ffb6c))
* Remove traces of semantic-release ([f0ab8ff](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/f0ab8ff070b620e5c9e6f69b3e5111e52f830427))
* Remove unnecessary include of py.typed from pyproject.toml ([#37](https://github.com/joveo/prometheus-fastapi-instrumentator/issues/37)) ([bbad45e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/bbad45ec1ab5baa0aca02e06857ee97ad466ab19))
* Rename poetry repo for TestPyPI ([3f1c500](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/3f1c500a69e90300056b7098b7a85ebe3efc19b5))
* Restructure poetry project layout ([b439ceb](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/b439ceb073703804156fcd42734cae3c7ffee59e))
* revert docs workflow change ([c166b3c](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/c166b3c42dbdea47536cee252d3092db52c5d0ed))
* Update changelog and bump version ([9ca4d67](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/9ca4d67ef6c6f270ee2a85881de8adee93c1f23b))
* Update gitignore ([e0fa528](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e0fa5286f841daac6486c0c3758c7edc1c30796e))
* Update Poetry to 1.3.0 ([8fef18e](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/8fef18e08ff5ad9b3428f9a7bd41ba9f650f3c95))
* Update pre-commit config ([e725750](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/e72575009fc628e9ccc8f39b74b16cd2028dd1f8))
* Update test release workflow ([23391e4](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/23391e4f7cd8743a2706184bf36dd537bf89e7ec))
* Update used CodeCov action version ([8813a55](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/8813a55ee8ed1475fb0010417717bef7d27086a3))
* upgrade setup-poetry action to v4 ([cc162b1](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/cc162b107ab2ed3d73c69c72c2aa1269256972ab))


### Styles

* apply auto stuff [skip ci] ([10f8ce7](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/10f8ce723c2b2803f69443729629d343e88ba6b2))
* apply auto stuff [skip ci] ([c18be90](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/c18be90a18203f4fe817e299990695bff9e6a20c))
* apply lint and format [skip ci] ([a6406ef](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/a6406ef4437d18967e881bb3be99359d8afd5d24))
* apply lint and format [skip ci] ([b435c63](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/b435c631f6881fe0d00d0ece34efc4ebd7a3ad6f))
* fix flake8 and mypy style findings ([761a3c1](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/761a3c10bc71e7ab31231e80a58c62c0d766f87c))
* remove unused import ([6341cb7](https://github.com/joveo/prometheus-fastapi-instrumentator/commit/6341cb749aa3d79142b624c96e09d17691b1fe3e))

## [5.9.1](https://github.com/trallnag/prometheus-fastapi-instrumentator/compare/v5.9.0...v5.9.1) (2022-08-23)


### 🍀 Summary 🍀

No bug fixes or new features. Just an important improvement of the documentation.


### ✨ Highlights ✨

* Fix / Improve documentation of how to use package ([#168](https://github.com/trallnag/prometheus-fastapi-instrumentator/pull/168)). Instrumentation should happen in a function decorated with `@app.on_event("startup")` to prevent crashes on startup. Thanks to @mdczaplicki and others.


### CI/CD

* Pin poetry version and improve caching configuration ([6337459](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/6337459156a9cd87d868953e6c6c8dabea064eb1))


### Docs

* Improve example in README on how to instrument app ([#168](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/168)) ([dc36aac](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/dc36aac1a530faa3970b19c1c68be4ee18c7c34b))


## [5.9.0](https://github.com/trallnag/prometheus-fastapi-instrumentator/compare/v5.8.2...v5.9.0) (2022-08-23)


### 🍀 Summary 🍀

This release fixes a small but annoying bug. Beyond that the release includes small internal improvements and bigger changes to CI/CD.


### ✨ Highlights ✨

* Removed print statement polluting logs ([#157](https://github.com/trallnag/prometheus-fastapi-instrumentator/pull/157)). Thanks to all the people raising this issue and to @nikstuckenbrock for fixing it.
* Added `py.typed` file to package to improve typing annotations ([#137](https://github.com/trallnag/prometheus-fastapi-instrumentator/pull/137)). Thanks to @mmaslowskicc for proposing and implementing this.
* Changed license from MIT to ISC, which is just like MIT but shorter.
* Migrated from Semantic Release to Release Please as release management tool.
* Overall refactoring of project structure to match my (@trallnag) template Python repo.
* Several improvements to the documentation. Thanks to @jabertuhin, @frodrigo, and @murphp15.
* Coding style improvements ([#155](https://github.com/trallnag/prometheus-fastapi-instrumentator/pull/155)). Replaced a few for loops with list comprehensions. Defaulting an argument to None instead of an empty list. Thanks to @yezz123.


### Features

* Add py.typed for enhanced typing annotations ([#37](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/37)) ([0c67d1b](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/0c67d1b8f51348979c00fd00d9457d3dd238df87))


### Bug Fixes

* Remove print statement from middleware ([#157](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/157)) ([f89792b](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/f89792b63d286e2ffd9241dc0b04c927f1102d07))


### Build

* **deps-dev:** bump devtools from 0.8.0 to 0.9.0 ([#172](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/172)) ([24bb060](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/24bb060a44b82b3b8d621d01af66dbd39773f2c7))
* **deps-dev:** bump flake8 from 4.0.1 to 5.0.4 ([#179](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/179)) ([8f72053](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/8f7205320ed648ef07fa21d7f699cf06cef3d4eb))
* **deps-dev:** bump mypy from 0.950 to 0.971 ([#174](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/174)) ([60e324f](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/60e324fb24f262f01f3d36be38c4e5e705523425))


### Docs

* Add missing colon to README ([#33](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/33)) ([faef24c](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/faef24c5aa4794cf1564ba871b15b736de303a86))
* Adjust changelog formatting ([b8b7b3e](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/b8b7b3ea2319947d8d5f9b8fb10c559267838516))
* Fix small typo in readme ([#154](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/154)) ([a569d4e](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/a569d4e58147a707c43e0fb698457c7ec7e13150))
* Move docs-internal to docs/devel and adjust contributing ([1b446ca](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/1b446ca3283514dcfbdaf9a1c5aa0f3a031ace45))
* Remove obsolete DEVELOPMENT.md ([1c18ff7](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/1c18ff72df97892680c9da7c0193997c6795dc83))
* Switch license from MIT to ISC ([1b0294a](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/1b0294ac03b3369cae9b6cc675b9c94e1a4c0d76))


### CI/CD

* Add .tool-versions ([255ba97](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/255ba97ee3dfbdada5fe300362b2725c075da0f8))
* Add codecov.yaml ([008ef61](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/008ef6136eba8d133a69de6f15ff14c39966fa2f))
* Add explicit codecov token ([b264184](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/b264184cea3bfdb318fb007ed0972814a41014eb))
* Adjust commitlint to allow more subject case types ([8b630aa](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/8b630aa2734696effe78e95ab638b08fb594c908))
* Correct default branch name ([5f141c5](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/5f141c59cc1b34b4cdbb2a77ba0edfc6c757356e))
* Improve and update scripts ([e1d9982](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/e1d998213b811c20f09e9c717efd2a97165b7939))
* Move to Release Please and refactor overall CI approach ([9977665](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/99776659515910a7c1369bcc7db916d440590ee7))
* Remove flake8 ignore W503 ([6eab3b8](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/6eab3b87fac913cf36b0266255304a917dec7b4f))
* Remove traces of semantic-release ([f0ab8ff](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/f0ab8ff070b620e5c9e6f69b3e5111e52f830427))
* Remove unnecessary include of py.typed from pyproject.toml ([#37](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/37)) ([bbad45e](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/bbad45ec1ab5baa0aca02e06857ee97ad466ab19))
* Rename poetry repo for TestPyPI ([3f1c500](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/3f1c500a69e90300056b7098b7a85ebe3efc19b5))
* Restructure poetry project layout ([b439ceb](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/b439ceb073703804156fcd42734cae3c7ffee59e))
* Update gitignore ([e0fa528](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/e0fa5286f841daac6486c0c3758c7edc1c30796e))
* Update pre-commit config ([e725750](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/e72575009fc628e9ccc8f39b74b16cd2028dd1f8))


### Refactor

* Improve coding style ([#155](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/155)) ([623d83b](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/623d83b86278d2627084b9fe9547f1af07531042))


## [5.8.2](https://github.com/trallnag/prometheus-fastapi-instrumentator/compare/v5.8.1...v5.8.2) (2022-06-12)

Refactored the middleware to an ASGI implementation ([#139](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/139)). Thanks to @Kludex and @adriangb for the proposal and implementation.


## [5.8.1](https://github.com/trallnag/prometheus-fastapi-instrumentator/compare/v5.8.0...v5.8.1) (2022-05-03)

Fixed a regression that made the required FastAPI version too strict for no reason ([#136](https://github.com/trallnag/prometheus-fastapi-instrumentator/issues/136)) ([36bc045](https://github.com/trallnag/prometheus-fastapi-instrumentator/commit/36bc045c5eb247fa7a83c25cc161f95b5d4b314d)). Thanks to @graipher for raising this issue.
