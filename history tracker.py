from collections import deque, Counter, defaultdict
from urllib.parse import urlparse

class HistoryTracker:
    def __init__(self, recent_capacity=10):
        self.recent = deque(maxlen=recent_capacity)  # most recent visits
        self.counter = Counter()                     # counts per hostname
        self.by_domain = defaultdict(list)           # full URLs per domain

    def visit(self, url: str):
        url = url.strip()
        if not url:
            return
        parsed = urlparse(url if "://" in url else "http://" + url)
        host = parsed.netloc.lower()
        self.recent.appendleft(url)
        self.counter[host] += 1
        self.by_domain[host].append(url)
        print(f"Visited: {url} (host: {host})")

    def show_recent(self):
        if not self.recent:
            print("No recent visits.")
            return
        print("\nRecent visits:")
        for i, u in enumerate(self.recent, 1):
            print(f"{i}. {u}")

    def show_top(self, n=5):
        print(f"\nTop {n} hosts:")
        for host, cnt in self.counter.most_common(n):
            print(f"{host}: {cnt} visits")

    def show_domain(self, domain):
        domain = domain.lower()
        urls = self.by_domain.get(domain, [])
        if not urls:
            print(f"No visits recorded for domain '{domain}'.")
            return
        print(f"\nVisits for {domain}:")
        for u in urls:
            print("-", u)

def main():
    ht = HistoryTracker(recent_capacity=10)
    print("Simple History Tracker")
    print("Commands: visit <url> | recent | top [n] | domain <host> | quit")
    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue
        parts = cmd.split(maxsplit=1)
        op = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""
        if op == "visit":
            ht.visit(arg)
        elif op == "recent":
            ht.show_recent()
        elif op == "top":
            try:
                n = int(arg) if arg else 5
            except ValueError:
                n = 5
            ht.show_top(n)
        elif op == "domain":
            ht.show_domain(arg)
        elif op in ("quit", "exit"):
            print("Bye.")
            break
        else:
            print("Unknown command. Use: visit, recent, top, domain, quit")

if __name__ == "__main__":
    main()