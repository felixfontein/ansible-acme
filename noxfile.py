# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Felix Fontein <felix@fontein.de>

# /// script
# dependencies = ["nox>=2025.02.09", "antsibull-nox"]
# ///

import os
import sys

import nox


try:
    import antsibull_nox
    import antsibull_nox.sessions
except ImportError:
    print("You need to install antsibull-nox in the same Python environment as nox.")
    sys.exit(1)


IN_CI = "GITHUB_ACTIONS" in os.environ


antsibull_nox.add_lint_sessions(
    run_isort=False,
    run_black=False,
    run_flake8=False,
    run_pylint=False,
    run_yamllint=True,
    yamllint_config=".yamllint",
    run_mypy=False,
)

antsibull_nox.add_docs_check(
    validate_collection_refs="all",
)

antsibull_nox.add_license_check()

antsibull_nox.add_extra_checks(
    run_no_unwanted_files=True,
    no_unwanted_files_module_extensions=[".py"],
    no_unwanted_files_yaml_extensions=[".yml"],
)

antsibull_nox.add_build_import_check(
    run_galaxy_importer=True,
)


# Allow to run the noxfile with `python noxfile.py`, `pipx run noxfile.py`, or similar.
# Requires nox >= 2025.02.09
if __name__ == "__main__":
    nox.main()
