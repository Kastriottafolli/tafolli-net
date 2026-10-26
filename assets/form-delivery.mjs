/* No credentials or mailbox access are required in the website. */
export async function deliverInquiry(endpoint, payload, {fetcher=fetch, timeoutMs=20000}={}) {
 const controller=new AbortController();
 const timeout=setTimeout(()=>controller.abort(),timeoutMs);
 try {
  const response=await fetcher(endpoint,{
   method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},
   credentials:'omit',body:JSON.stringify(payload),signal:controller.signal
  });
  const data=await response.json();
  if(response.ok&&(data.success===true||data.success==='true'))return;
  throw new Error(/activat|confirm.*email|verify/i.test(String(data.message||''))?'activation':'delivery');
 } finally {clearTimeout(timeout);}
}

