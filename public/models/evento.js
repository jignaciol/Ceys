var ceys = ceys || {}

ceys.models.evento = Backbone.Model.extend({

    urlRoot: "/api/evento",

    defaults: {
        id_persona: 0,
        event_date: "",
        event_time: "",
        ubicacion: "",
        bl: 0
    }

})
