```mermaid

flowchart TD
    A[MQTT bericht ontvangen] --> B[JSON payload decoden]
    B --> C[player_id, x, y en type uitlezen]
    C --> D{Bestaat speler al in players?}

    D -->|Nee| E[Nieuwe speler toevoegen met x, y en kleur]
    D -->|Ja| F[Speler positie updaten]

    E --> G{Is message_type join en niet mijn eigen player_id?}
    F --> G

    G -->|Ja| H[Publiceer mijn eigen positie terug]
    G -->|Nee| I[Niets terugsturen]

    H --> J[Einde on_message]

```