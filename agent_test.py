from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)
from llama_index.utils.workflow import draw_all_possible_flows



class MyWorkflow(Workflow):
    @step
    async def my_step(self, ev: StartEvent) -> StopEvent:
        a = 30+7
        return StopEvent(result=f"Hello, Tor Odin! {a}")


async def main():
    w = MyWorkflow(timeout=10, verbose=False)
    result = await w.run()
    print(result)

draw_all_possible_flows(MyWorkflow, filename="multi_step_workflow.html")
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())


## https://docs.llamaindex.ai/en/stable/understanding/workflows/basic_flow/
