import test from 'node:test';
import assert from 'node:assert/strict';
import {calculate,scaling,catalog} from '../assets/planner-model.mjs';

test('the example separates setup and recurring costs and subtracts existing leads',()=>{
 const plan=calculate();
 // 500/2 paid + 2500*1% social + 150 SEO + 500*10% local = 475 added visits.
 // (300+475)*3% - 300*2% = 17.25 added enquiries; 25% close = 4.3125.
 assert.equal(plan.once,2500);assert.equal(plan.monthly,2000);
 assert.equal(plan.addedVisits,475);assert.equal(plan.impressions,15500);
 assert.equal(plan.addedLeads,17.25);assert.equal(plan.customers,4.3125);
});
test('no selected services create no additional budget or results',()=>{
 const plan=calculate({active:{website:false,social:false,seo:false,local:false,ads:false}});
 for(const key of ['once','monthly','addedVisits','addedLeads','customers','low','high'])assert.equal(plan[key],0);
});
test('doubling media spend doubles the paid contribution at unchanged assumptions',()=>{
 const input={active:{website:false,social:false,seo:false,local:false,ads:true},values:{ads:400,cpc:2,baseCvr:2,closeRate:25}};
 const plan=calculate(input);
 assert.equal(plan.addedVisits,200);assert.equal(plan.customers,1);
 assert.deepEqual(scaling(input,[0,400,800]).map(row=>row.customers),[0,1,2]);
});
test('a website budget alone buys no additional traffic',()=>{
 const plan=calculate({active:{website:true,social:false,seo:false,local:false,ads:false},values:{baseVisitors:300,baseCvr:2,targetCvr:3,closeRate:25}});
 assert.equal(plan.addedVisits,0);assert.equal(plan.impressions,0);
 assert.equal(plan.addedLeads,3);assert.equal(plan.customers,.75);
});
test('organic assumptions do not rise automatically with service budgets',()=>{
 const first=calculate(),second=calculate({values:{social:1500,seo:2000,local:300}});
 assert.equal(first.channels.social,second.channels.social);assert.equal(first.channels.seo,second.channels.seo);
 assert.ok(second.monthly>first.monthly);
});
test('invalid inputs stay bounded and cannot cause infinite results',()=>{
 const plan=calculate({values:{cpc:0,socialCtr:200,ads:-1,seoVisits:Infinity}});
 assert.equal(plan.values.cpc,.1);assert.equal(plan.values.socialCtr,100);assert.equal(plan.values.ads,0);
 for(const value of Object.values(plan))if(typeof value==='number')assert.ok(Number.isFinite(value));
});
test('worse conversion assumptions can show fewer customers',()=>{
 const plan=calculate({active:{website:true,social:false,seo:false,local:false,ads:false},values:{baseVisitors:1000,baseCvr:5,targetCvr:1,closeRate:50}});
 assert.equal(plan.customers,-20);assert.ok(plan.low<=plan.high);assert.ok(plan.high<0);
});
test('minimum budgets apply to all supported website types and recurring services',()=>{
 for(const type of catalog.websiteTypes){
  const plan=calculate({websiteType:type.id,values:{website:0,seo:0,local:0}});
  assert.equal(plan.once,type.min);assert.equal(plan.websiteType.id,type.id);
  assert.equal(plan.values.seo,450);assert.equal(plan.values.local,550);
 }
 const off=calculate({active:{website:false,seo:false,local:false}});
 assert.equal(off.once,0);assert.equal(off.monthly,1000);
});
test('website type and setup cost never manufacture visits or customers',()=>{
 const a=calculate({websiteType:'mini'}),b=calculate({websiteType:'commerce',values:{website:100000}});
 assert.equal(a.once,2500);assert.equal(b.once,100000);
 assert.equal(a.customers,b.customers);assert.equal(a.addedVisits,b.addedVisits);
 assert.deepEqual(scaling(a,[0,500,1000]),scaling(b,[0,500,1000]));
 assert.equal(calculate({websiteType:'unknown'}).websiteType.id,catalog.defaultWebsiteType);
});
