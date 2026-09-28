from dataclasses import dataclass


@dataclass
class TextChunk:
    chunk_id: int
    text: str
    page_number: int | None = None


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[TextChunk]:
    if not text.strip():
        return []

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(
                TextChunk(
                    chunk_id=chunk_id,
                    text=chunk,
                )
            )
            chunk_id += 1

        if end >= len(text):
            break

        start = end - overlap

    return chunks
