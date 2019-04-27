# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have
# "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When
# we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and
# "com" implicitly.

# Now, call a "count-paired domain" to be a count (representing the number of visits this domain
# received), followed by a space, followed by the address. An example of a count-paired domain might be
# "9001 discuss.leetcode.com".

# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
# (in the same format as the input, and in any order), that explicitly counts the number of visits to
# each subdomain.

# Example 1:
# Input:
# ["9001 discuss.leetcode.com"]
# Output:
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

# Example 2:
# Input:
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]


class Solution:
    def subdomainVisits(self, cpdomains: 'List[str]') -> 'List[str]':
        dmcount = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count, domain = int(count), domain.split('.')

            for i in range(len(domain)):
                sbdomain = '.'.join(domain[i:])
                if sbdomain not in dmcount:
                    dmcount[sbdomain] = count
                else:
                    dmcount[sbdomain] += count

        return [str(count) + " " + sbdomain for sbdomain, count in dmcount.items()]