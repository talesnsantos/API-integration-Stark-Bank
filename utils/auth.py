import starkbank


def auth():
    private_key_content = """ """

    project =starkbank.Project(
        environment="sandbox",
        id="5005790997905408",
        private_key=private_key_content
    )
    starkbank.user = project