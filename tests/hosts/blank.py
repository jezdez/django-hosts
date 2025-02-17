from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(r"", "tests.urls.simple", name="blank"),
    host(r"|www", "tests.urls.simple", name="blank_or_www"),
)
