var ceys = ceys || {}

ceys.models.persona = Backbone.Model.extend({

    urlRoot: "/api/persona",

    defaults: {
        voe: "",
        cedula: "",
        nombre: "",
        apellido: "",
        bl: 0
    }

})
