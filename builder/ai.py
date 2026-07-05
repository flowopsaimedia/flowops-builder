from builder.context import module_context
from builder.content_generator import build_business_system


def preview(module_id):

    context = module_context(module_id)

    return build_business_system(context)