# License AGPLv3 (https://www.gnu.org/licenses/agpl-3.0-standalone.html)
import os
import setuptools


here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()


setuptools.setup(
    name="oca-maintainers-tools",
    author="Odoo Community Association (OCA)",
    description="Set of tools to help managing Odoo Community projects",
    long_description=long_description,
    license="AGPL3",
    packages=["tools"],
    include_package_data=True,
    zip_safe=False,
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "appdirs",
        "click",
        "docutils",
        "pypandoc",  # for oca-gen-addon-readme to work with markdown fragments
        "ERPpeek",
        "freezegun",
        "github3.py>=1",
        "jinja2",
        "manifestoo-core>=1.1",
        "PyYAML",
        "polib",
        "pygments",
        "requests",
        "toml>=0.10.0",  # for oca-towncrier
        "tomli ; python_version < '3.11'",  # from 3.11 tomllib is in stdlib
        "towncrier>=21.3",  # for oca-towncrier
        "selenium",
        "twine",
        "wheel",
        "pyproject_dependencies ; python_version>='3.7'",
        "setuptools-odoo",  # for oca-gen-external-dependencies
        "whool",  # for oca-gen-external-dependencies
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: "
        "GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    entry_points={
        "console_scripts": [
            "witech-github-login = tools.github_login:main",
            "witech-copy-maintainers = tools.copy_maintainers:main",
            "witech-clone-everything = tools.clone_everything:main",
            "witech-set-repo-labels = tools.set_repo_labels:main",
            "witech-odoo-login = tools.odoo_login:main",
            "witech-sync-users = tools.oca_sync_users:main",
            "witech-gen-addons-table = tools.gen_addons_table:gen_addons_table",
            "witech-migrate-branch = tools.migrate_branch:main",
            "witech-migrate-branch-empty = tools.migrate_branch_empty:main",
            "witech-publish-modules = tools.publish_modules:main",
            "witech-gen-addon-readme = tools.gen_addon_readme:gen_addon_readme",
            "witech-gen-addon-icon = tools.gen_addon_icon:gen_addon_icon",
            "witech-gen-external-dependencies = tools.gen_external_dependencies:main",
            "witech-gen-metapackage = tools.gen_metapackage:main",
            "witech-towncrier = tools.oca_towncrier:oca_towncrier",
            "witech-create-migration-issue = tools.create_migration_issue:main",
            "witech-update-pre-commit-excluded-addons = "
            "tools.update_pre_commit_excluded_addons:main",
            "witech-fix-manifest-website = tools.fix_manifest_website:main",
            "witech-configure-travis= tools.configure_travis:main",
            "witech-create-branch = tools.create_branch:main",
            "witech-copier-update = tools.copier_update:main",
        ],
    },
)
