// A transparent scenario model, not a price list or a forecast of actual results.
export const defaults=Object.freeze({website:2500,social:500,seo:350,local:100,ads:500,baseVisitors:300,socialViews:2500,socialCtr:1,seoVisits:150,localViews:500,localCtr:10,cpc:2,adCtr:2,baseCvr:2,targetCvr:3,closeRate:25});
const limits={website:[0,100000],social:[0,20000],seo:[0,20000],local:[0,10000],ads:[0,50000],baseVisitors:[0,1000000],socialViews:[0,10000000],socialCtr:[0,100],seoVisits:[0,1000000],localViews:[0,1000000],localCtr:[0,100],cpc:[.1,100],adCtr:[.1,100],baseCvr:[0,100],targetCvr:[0,100],closeRate:[0,100]};
export function normalize(input={}){
 const values={};
 for(const [key,fallback] of Object.entries(defaults)){const value=Number(input.values?.[key]??fallback),[min,max]=limits[key];values[key]=Math.max(min,Math.min(max,Number.isFinite(value)?value:fallback));}
 const active=Object.fromEntries(['website','social','seo','local','ads'].map(key=>[key,input.active?.[key]!==false]));
 return {active,values};
}
export function calculate(input={}){
 const {active:a,values:v}=normalize(input);
 const paidVisits=a.ads?v.ads/v.cpc:0;
 const socialViews=a.social&&v.social>0?v.socialViews:0,localViews=a.local&&v.local>0?v.localViews:0;
 const socialVisits=socialViews*v.socialCtr/100,localVisits=localViews*v.localCtr/100;
 const seoVisits=a.seo&&v.seo>0?v.seoVisits:0;
 const addedVisits=paidVisits+socialVisits+localVisits+seoVisits,totalVisits=v.baseVisitors+addedVisits;
 const effectiveCvr=a.website?v.targetCvr:v.baseCvr;
 const baseLeads=v.baseVisitors*v.baseCvr/100,totalLeads=totalVisits*effectiveCvr/100;
 const addedLeads=totalLeads-baseLeads,customers=addedLeads*v.closeRate/100;
 const bounds=[customers*.75,customers*1.25];
 const impressions=paidVisits/(v.adCtr/100)+socialViews+localViews;
 const monthly=['social','seo','local','ads'].reduce((sum,key)=>sum+(a[key]?v[key]:0),0);
 return {active:a,values:v,once:a.website?v.website:0,monthly,impressions,addedVisits,totalVisits,addedLeads,customers,low:Math.floor(Math.min(...bounds))||0,high:Math.ceil(Math.max(...bounds))||0,channels:{paid:paidVisits,social:socialVisits,seo:seoVisits,local:localVisits},effectiveCvr};
}
export function scaling(input={},amounts=[0,500,1000,1500,2000]){
 const model=normalize(input);
 return amounts.map(budget=>({budget,customers:calculate({active:{...model.active,ads:true},values:{...model.values,ads:budget}}).customers}));
}
