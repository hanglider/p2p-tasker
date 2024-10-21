def a(x, y):
    for func in self.funcs:
            task = asyncio.to_thread(func(**self.kwargs))
            tasks.append(asyncio.create_task(func(**self.kwargs)))