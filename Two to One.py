def longest(s1, s2):
    s3 = s1 + s2
    s3 = set(s3)
    s3 = list(s3)
    s3.sort()
    return "". join(s3)
