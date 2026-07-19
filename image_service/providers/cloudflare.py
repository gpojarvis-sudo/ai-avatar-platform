import base64
import httpx
from loguru import logger
from config.settings import settings
from .base import BaseImageProvider

class CloudflareProvider(BaseImageProvider):
    PROVIDER_NAME="cloudflare"
    async def generate(self,prompt:str,**kwargs):
        model=settings.CLOUDFLARE_IMAGE_MODEL
        url=f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ACCOUNT_ID}/ai/run"
        headers={"Authorization":f"Bearer {settings.CLOUDFLARE_API_TOKEN}","Content-Type":"application/json"}
        payload={"model":model,"input":{"prompt":prompt,"aspect_ratio":kwargs.get("aspect_ratio","1:1")}}
        try:
            async with httpx.AsyncClient(timeout=180) as client:
                r=await client.post(url,headers=headers,json=payload)
                r.raise_for_status();data=r.json()
            if data.get("state")!="Completed":
                return {"success":False,"provider":self.PROVIDER_NAME,"model":model,"error":str(data)}
            img=data["result"]["image"]
            if not img.startswith("data:image"): raise ValueError("Unexpected image format")
            b=base64.b64decode(img.split(",",1)[1])
            return {"success":True,"provider":self.PROVIDER_NAME,"model":model,"image_bytes":b}
        except Exception as e:
            logger.exception(e)
            return {"success":False,"provider":self.PROVIDER_NAME,"model":model,"error":str(e)}
