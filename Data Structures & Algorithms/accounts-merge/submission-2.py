class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(list)

        for account in accounts:
            src = account[1]
            adj_list[src]

            for dest in account[2:]:
                adj_list[src].append(dest)
                adj_list[dest].append(src)

        out, merged_account, visited = [], [], set()
        def dfs(email):
            if email in visited:
                return
            
            visited.add(email)
            merged_account.append(email)
            for connected_email in adj_list[email]:
                dfs(connected_email)
            
        for account in accounts:
            if account[1] in visited:
                continue
            merged_account = []
            dfs(account[1])
            merged_account.sort()
            out.append([account[0], *merged_account])

        return out
            