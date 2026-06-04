class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack represents each directory
        directories = []
        split_path = path.split("/")
        print(split_path)

        for arg in split_path:
            if arg == "" or arg == ".":
                continue
            elif arg == "..":
                if directories:
                    directories.pop()
            else:
                directories.append(arg)
                arg = ""

        out = f"/{"/".join(directories)}" if directories else "/"
        return out
        