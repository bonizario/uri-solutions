def main():
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        connections = 0
        servers = dict()
        known_apps = set()
        for i in range(n):
            total_apps, *apps = input().split()
            servers[i] = set(apps)
            known_apps.update(servers[i])
        for _ in range(m):
            total_apps, *apps = input().split()
            for server_id in servers:
                for app in set(apps):
                    if app in known_apps and app in servers[server_id]:
                        connections += 1
                        break
        print(connections)
main()
