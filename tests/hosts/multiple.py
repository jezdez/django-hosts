from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(r"spam\.eggs", "tests.urls.multiple", name="multiple"),
)
