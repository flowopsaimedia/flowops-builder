from builder.knowledge import workflows


def module_context(module_id):

    data = workflows()

    return {

        "module": module_id,

        "systems": data[module_id]

    }