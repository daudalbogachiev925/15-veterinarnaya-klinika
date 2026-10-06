CREATE TABLE owners (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT
);

CREATE TABLE pets (
    id BIGSERIAL PRIMARY KEY,
    owner_id BIGINT REFERENCES owners(id),
    species TEXT NOT NULL,
    breed TEXT,
    name TEXT NOT NULL,
    birth DATE,
    weight NUMERIC(5,2),
    chip TEXT UNIQUE
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE vets (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    spec TEXT,
    cabinet TEXT
);

CREATE TABLE visits (
    id BIGSERIAL PRIMARY KEY,
    pet_id BIGINT REFERENCES pets(id),
    vet_id BIGINT REFERENCES vets(id),
    service_id INT REFERENCES services(id),
    diagnosis TEXT,
    visit_date TIMESTAMP DEFAULT NOW(),
    price NUMERIC(10,2),
    notes TEXT
);

CREATE TABLE vaccines (
    id BIGSERIAL PRIMARY KEY,
    pet_id BIGINT REFERENCES pets(id),
    vaccine TEXT NOT NULL,
    given DATE NOT NULL,
    next_due DATE,
    vet_id BIGINT REFERENCES vets(id)
);

CREATE INDEX idx_visits_pet ON visits(pet_id);
CREATE INDEX idx_visits_date ON visits(visit_date);
CREATE INDEX idx_vaccines_pet ON vaccines(pet_id);
