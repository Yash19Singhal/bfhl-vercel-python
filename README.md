## Endpoint
- Production URL:  
  `https://bfhl-vercel-python-1.vercel.app/bfhl`


- User details:
  - user_id: `yash_singhal_19092004`
  - email: `singhalyash340@gmail.com`
  - roll_number: `22BCE0807`

## Local test with Vercel CLI
```
npm i -g vercel
vercel dev
curl -X POST http://localhost:3000/bfhl -H "Content-Type: application/json" -d '{"data":["a","1","334","4","R","$"]}'
```
