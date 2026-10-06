SELECT p.name AS pet, o.full_name AS owner,
       v.vaccine, v.given, v.next_due,
       v.next_due - CURRENT_DATE AS days_left
FROM vaccines v
JOIN pets p ON p.id = v.pet_id
JOIN owners o ON o.id = p.owner_id
WHERE v.next_due <= CURRENT_DATE + INTERVAL '60 days'
ORDER BY v.next_due;
