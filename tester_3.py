from trl.agents.utils import AsyncE2BExecutor,LocalExecutor

executor = AsyncE2BExecutor(api_key="e2b_9f17248b4c30dac21400e155f031824e180e5a09",max_concurrent=5)


sleeping_code = [
    "import time; time.sleep(3); print('Task 1')",
    "import time; time.sleep(3); print('Task 2')",
    "import time; time.sleep(3); print('Task 3')",
    "import time; time.sleep(3); print('Task 4')",
    "import time; time.sleep(3); print('Task 5')",
]

results = executor.execute(sleeping_code)

print(results)