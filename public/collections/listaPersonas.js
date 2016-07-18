var ceys = ceys || {}

ceys.collections.listaPersona = Backbone.Collection.extend({

    url: "/api/persona",

    model: ceys.models.persona,

    getByCedula: function(cedula) {
        var newPerson = new ceys.models.persona()
        this.each(function(persona){
            if (persona.get("cedula") == cedula){
                newPerson.set({
                    voe: persona.get("voe"),
                    cedula: persona.get("cedula"),
                    nombre: persona.get("nombre"),
                    apellido: persona.get("apellido"),
                    bl: persona.get("bl")
                })
            }
        })
        return newPerson
    }

})
