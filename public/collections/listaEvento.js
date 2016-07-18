var ceys = ceys || {}

ceys.collections.listaEvento = Backbone.Collection.extend({

    url: "/api/evento",

    model: ceys.models.evento

})
