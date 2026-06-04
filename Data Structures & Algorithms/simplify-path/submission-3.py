class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        split_path = path.split("/")

        for arg in split_path:
            if arg == "" or arg == ".":
                continue
            elif arg == "..":
                if directories:
                    directories.pop()
            else:
                directories.append(arg)

        return "/" + "/".join(directories)
        