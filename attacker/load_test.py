import asyncio
import httpx
import json
from rich import print
from datetime import datetime

URL = "http://127.0.0.1:8000/api"
TOTAL_REQUESTS = 1000
CONCURRENCY = 50

success = 0
fail = 0

async def worker(client):
    global success, fail
    try:
        response = await client.get(URL)
        if response.status_code == 200:
            success += 1
        else:
            fail += 1
    except Exception:
        fail += 1

async def main():
    global success, fail

    async with httpx.AsyncClient(timeout=5.0) as client:
        tasks = []

        for _ in range(TOTAL_REQUESTS):
            tasks.append(worker(client))

            if len(tasks) >= CONCURRENCY:
                await asyncio.gather(*tasks)
                tasks = []

        if tasks:
            await asyncio.gather(*tasks)

    print(f"[green]Sucesso:[/green] {success}")
    print(f"[red]Falhas:[/red] {fail}")

    # salvar resultados
    data = {
        "timestamp": datetime.now().isoformat(),
        "success": success,
        "fail": fail
    }

    with open("analytics/results.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    asyncio.run(main())