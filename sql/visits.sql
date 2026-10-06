SELECT v.id, p.name AS pet, o.full_name AS owner,
       ve.full_name AS vet, s.name AS service,
       v.diagnosis, v.price, v.visit_date
FROM visits v
JOIN pets p ON p.id = v.pet_id
JOIN owners o ON o.id = p.owner_id
JOIN vets ve ON ve.id = v.vet_id
JOIN services s ON s.id = v.service_id
WHERE v.visit_date >= NOW() - INTERVAL '30 days'
ORDER BY v.visit_date DESC;
