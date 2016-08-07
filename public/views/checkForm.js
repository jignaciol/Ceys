var ceys = ceys || {}

ceys.views.checkForm = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("checkForm") ),

    render: function() {
        this.$el.html( this.template() )
        return this
    },

    initialize: function() {
        this.render()
    }

})
