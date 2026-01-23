from PIL import Image
import io, os, uuid

def convert_and_compress(image_bytes, min_kb, max_kb):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    low, high = 20, 95
    best_quality = 85

    while low <= high:
        q = (low + high) // 2
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=q)
        size_kb = buf.tell() / 1024

        if min_kb <= size_kb <= max_kb:
            best_quality = q
            break
        elif size_kb > max_kb:
            high = q - 1
        else:
            low = q + 1

    os.makedirs("temp", exist_ok=True)
    path = f"temp/{uuid.uuid4().hex}.jpg"
    img.save(path, "JPEG", quality=best_quality)

    final_size = os.path.getsize(path) / 1024
    status = "OK" if min_kb <= final_size <= max_kb else "OUT_OF_RANGE"

    return path, round(final_size, 2), status
