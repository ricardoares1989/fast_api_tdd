from ..models.pydantic import SummaryPayloadSchema
from ..models.tortoise import TextSummary

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id
