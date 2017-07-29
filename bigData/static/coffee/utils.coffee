(($) ->
  class Utilities
    constructor: ->
      @baseGeoOpenDataApiUrl = 'https://opencouncildata.cloudant.com/test1/_design/geo/_geo/'

    makeChart: (container, highChartsData) ->
      $(container).highcharts highChartsData


    initializeLobiPanel: ->
      $('#lobipanel-multiple').find('.tile .panel').lobiPanel
        sortable: true
        reload: false
        editTitle: false
        unpin: false
        minimize: false


    getTileData: (postCodes, type, cb) ->
      $.ajax
        url: '/getTile/'
        method: 'GET'
        data: {postCodes, type}
        contentType: 'application/json'
        success: (htmlCode) -> cb null, htmlCode


    addTile: (htmlCode) =>
      newTile = $ htmlCode
      $('#first_col').prepend newTile

      $ => @initializeLobiPanel()


    callOpenCouncilDataApi: (url, cb) ->
      $.ajax
        url: url,
        method: 'GET'
        dataType: 'json'
        success: (data) -> cb null, data
        fail: (xhr, status, error) -> cb {xhr, status, error}, null


    getNumberOfParks: (postcode, cb) =>
      $.ajax
        url: '/getPostcode'
        method: 'GET'
        data: {code: postcode}
        dataType: 'json'
        success: (data) =>
          {latitude, longitude} = data[0].fields
          url = "#{@baseGeoOpenDataApiUrl}/parks?lat=#{latitude.trim()}&lon=#{longitude.trim()}&radius=10000"
          @callOpenCouncilDataApi url, (err, data) ->
            if (err == null) then cb null, data.rows.length else cb err, data


    renderTile: (templateName, data) =>
      $.ajax
        url: '/getTemplate/'
        method: 'POST'
        data: JSON.stringify {templateName, data}
        success: (htmlCode) => @addTile htmlCode


  $.utilities = new Utilities()
) jQuery
