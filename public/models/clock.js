var ceys = ceys || {}

ceys.models.clock = Backbone.Model.extend({

    date: new Date(),

    defaults: {
        hour: "",
        weekday: "",
        day: "",
        month: ""
    }

})
