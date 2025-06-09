from src.magneto import container


async def simulate(design_id: int):
    return container.simulations.simulate(design_id)
