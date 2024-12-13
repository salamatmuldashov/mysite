1. **Indexes**:
   - Added indexes on frequently queried fields (e.g., `Product.category`).

2. **Query Optimization**:
   - Used `select_related` for one-to-one and foreign key relationships.


3. **Schema Design**:
   - Normalized database schema to avoid redundancy and ensure referential integrity.

4. **Caching**:
   - Used Redis for caching frequently accessed data (`/api/products/`, `/api/products/<id>`).

5. **Scalability**:
   - Use read replicas for scaling read operations.
   - Partition large tables if necessary.