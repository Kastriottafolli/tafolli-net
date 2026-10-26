import test from 'node:test';
import assert from 'node:assert/strict';
import {deliverInquiry} from '../assets/form-delivery.mjs';

const endpoint='https://example.invalid/form';
const response=(success,ok=true,message='')=>async()=>({ok,json:async()=>({success,message})});

test('accepts a confirmed provider response and transmits the complete payload',async()=>{
 const payload={name:'Test',email:'info@example.invalid',Planung:'Selected services and assumptions'};
 await deliverInquiry(endpoint,payload,{fetcher:async(url,options)=>{
  assert.equal(url,endpoint);assert.equal(options.method,'POST');
  assert.equal(options.credentials,'omit');assert.deepEqual(JSON.parse(options.body),payload);
  return {ok:true,json:async()=>({success:'true'})};
 }});
});
test('recognizes the provider activation failure',async()=>{
 await assert.rejects(deliverInquiry(endpoint,{}, {fetcher:response('false',true,'This form needs Activation')}),/activation/);
});
test('does not accept an HTTP error as successful delivery',async()=>{
 await assert.rejects(deliverInquiry(endpoint,{}, {fetcher:response(true,false)}),/delivery/);
});
test('does not accept an unconfirmed response',async()=>{
 await assert.rejects(deliverInquiry(endpoint,{}, {fetcher:response(false)}),/delivery/);
});
test('invalid JSON and network errors remain failures',async()=>{
 await assert.rejects(deliverInquiry(endpoint,{}, {fetcher:async()=>({ok:true,json:async()=>{throw new SyntaxError('invalid JSON')}})}),SyntaxError);
 await assert.rejects(deliverInquiry(endpoint,{}, {fetcher:async()=>{throw new Error('offline')}}),/offline/);
});
test('aborts an unresponsive request',async()=>{
 await assert.rejects(deliverInquiry(endpoint,{}, {timeoutMs:5,fetcher:async(url,{signal})=>new Promise((resolve,reject)=>signal.addEventListener('abort',()=>reject(new Error('aborted')),{once:true}))}),/aborted/);
});
