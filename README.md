# BFHL – Vercel Python (Final)

- Endpoint: POST `/bfhl`
- Handler file: `api/bfhl.py`
- Rewrite: `/bfhl` → `/api/bfhl` in `vercel.json`
- User details baked in:
  - user_id: `yash_singhal_19092004`
  - email: `singhalyash340@gmail.com`
  - roll_number: `22BCE0807`

## Local test with Vercel CLI
```
npm i -g vercel
vercel dev
curl -X POST http://localhost:3000/bfhl -H "Content-Type: application/json" -d '{"data":["a","1","334","4","R","$"]}'
```
