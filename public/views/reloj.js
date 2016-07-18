var ceys = ceys || {}

ceys.views.reloj = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("reloj") ) ,

    render: function() {
        clock = new ceys.models.clock()
        this.$el.html(this.template(clock.toJSON()))
    },

    initialize: function() {
        this.render()
    }

})
