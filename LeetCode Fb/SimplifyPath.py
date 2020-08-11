"""
    Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

    In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

    Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between
    two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path
    must be the shortest string representing the absolute path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:

        # Handle empty string (edge case)
        if not str:
            return str

        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            # in case you find a dot or you find a '/'
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stitch together all the directory names together
        # the double "/" + "/" are necessary, so the result is
        # displayed as / at the beginning

        final_str = "/" + "/".join(stack)
        return final_str


def main():
    s = '/home/..'
    solution = Solution()
    res = solution.simplifyPath(s)
    print(res)


main()