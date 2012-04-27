{
    xtype: 'formautoload',
    layout: 'anchor',
    autoScroll: true,
    trackResetOnLoad: true,
    bodyPadding: '10 25 10 10',//padding on the right side 25 for scrollbar
    height: '100%',
    url: '/annotation/api/annotationview/?_accept=application/json&include_geom=true&action={% if annotation %}update{% else %}create{% endif %}',
    {% if annotation %}
    loadProxy: {
        url: '/annotation/api/annotationform/',
        type: 'ajax',
        method: 'GET',
        reader: {
          root: 'data',
          type: 'json'
        },
        params: {
            include_geom: true,
            flat: false,
            _accept: 'application/json',
            object_id: {{ annotation.id }}
        },
        success: function(form, action) {
            console.log('success gives:');
            console.log(arguments);
        },
        failure: function(form, action) {
            Ext.Msg.alert("Load failed", action.result.errorMessage);
        }
    },
{% else %}
    loadData: {
    {% if init_parent %}
        parent: {id:{{ init_parent.id }}, name:'{{ init_parent.title }}'},
    {% endif %}
    {% if init_waterbody %}
        waterbodies: {id:{{ init_waterbody.id }}, name:'{{ init_waterbody.name }}'},
    {% endif %}
    {% if init_area %}
        areas: {id:{{ init_area.id }}, name:'{{ init_area.name }}'},
    {% endif %}
        test: 'extra for comma'
    },
{% endif %}
    items:[
        {
            name: 'id',
            xtype: 'hiddenfield'
        },
        {
            fieldLabel: 'Titel',
            name: 'title',
            width: 600,
            xtype: 'textfield',
            allowBlank: false
        },
        {
            fieldLabel: 'Omschrijving',
            name: 'description',
            anchor: '100%',
            xtype: 'htmleditor',
            allowBlank: false,
        },
        {
            fieldLabel: 'Categorie',
            name: 'annotation_category',
            displayField: 'name',
            valueField: 'id',
            width: 400,
            xtype: 'combodict',
            store: {
                fields: ['id', 'name'],
                data: Ext.JSON.decode(
                  {% autoescape off %}
                  '{{ annotation_categories }}'
                  {% endautoescape %})
            },
            multiSelect: false,
            forceSelection: true,
            allowBlank: false
        },
        {
            fieldLabel: 'Status',
            name: 'annotation_status',
            displayField: 'name',
            valueField: 'id',
            width: 400,
            xtype: 'combodict',
            store: {
                fields: ['id', 'name'],
                data: Ext.JSON.decode(
                  {% autoescape off %}
                  '{{ annotation_statuses }}'
                  {% endautoescape %})
            },
            multiSelect: false,
            forceSelection: true,
            allowBlank: false
        },
        {
            fieldLabel: 'Waarneming van',
            name: 'datetime_period_start',
            width: 200,
            xtype: 'datefield',
            allowBlank: false,
            format: 'd-m-Y',
            altFormats: 'Y-m-d h:m:s',
            submitFormat: 'Y-m-d h:m:s'
        },
        {
            fieldLabel: 'tot',
            name: 'datetime_period_end',
            width: 200,
            xtype: 'datefield',
            allowBlank: false,
            format: 'd-m-Y',
            altFormats: 'Y-m-d h:m:s',
            submitFormat: 'Y-m-d h:m:s'
        },
        {
            xtype:'fieldset',
            collapsible: true,
            title: 'Gerelateerde objecten',
            collapsed: false,
            layout: 'anchor',
            defaults: {
                anchor: '100%'
            },
            items: [
                {
                    xtype: 'combomultiselect',
                    fieldLabel: 'aan/ afvoer gebieden',
                    name: 'areas',
                    field_name: 'aan/ afvoer gebieden',
                    read_at_once: false,
                    combo_store: {
                        fields: [
                            {name: 'id', mapping: 'id' },
                            {name: 'name', mapping: 'name' }
                        ],
                        proxy: {
                            type: 'ajax',
                            url: '/area/api/catchment-areas/?_accept=application%2Fjson&size=id_name&flat=true',
                            reader: {
                                type: 'json',
                                root: 'areas'
                            }
                        }
                    }
                },
                {
                    xtype: 'combomultiselect',
                    fieldLabel: 'KRW waterlichamen',
                    name: 'waterbodies',
                    field_name: 'KRW waterlichamen',
                    read_at_once: false,
                    combo_store: {
                        fields: [
                            {name: 'id', mapping: 'id' },
                            {name: 'name', mapping: 'name' }
                        ],
                        proxy: {
                            type: 'ajax',
                        url: '/measure/api/waterbody/?node=root&_accept=application%2Fjson&size=id_name',
                            reader: {
                                type: 'json',
                                root: 'data'
                            }
                        }
                    }
                },
                {
                    xtype: 'combomultiselect',
                    fieldLabel: 'Maatregelen',
                    name: 'measures',
                    field_name: 'Maatregelen',
                    read_at_once: false,
                    combo_store: {
                        fields: [
                            {name: 'id', mapping: 'id' },
                            {name: 'name', mapping: 'name' }
                        ],
                        proxy: {
                            type: 'ajax',
                        url: '/measure/api/measure/?node=root&_accept=application%2Fjson&size=id_name&include_geom=false',
                            reader: {
                                type: 'json',
                                root: 'data'
                            }
                        }
                    }
                },
                {
                    xtype: 'combomultiselect',
                    fieldLabel: 'Workspaces',
                    name: 'workspaces',
                    field_name: 'Workspaces',
                    read_at_once: false,
                    combo_store: {
                        fields: [
                            {name: 'id', mapping: 'id' },
                            {name: 'name', mapping: 'name' }
                        ],
                        proxy: {
                            type: 'ajax',
                            url: '/workspace/api/workspace_view/?node=root&_accept=application%2Fjson&size=id_name',
                            reader: {
                                type: 'json',
                                root: 'data'
                            }
                        }
                    }
                },
                {
                    xtype: 'combomultiselect',
                    fieldLabel: 'Collages',
                    name: 'collages',
                    field_name: 'Collages',
                    read_at_once: false,
                    combo_store: {
                        fields: [
                            {name: 'id', mapping: 'id' },
                            {name: 'name', mapping: 'name' }
                        ],
                        proxy: {
                            type: 'ajax',
                            url: '/workspace/api/collage_view/?node=root&_accept=application%2Fjson&size=id_name',
                            reader: {
                                type: 'json',
                                root: 'data'
                            }
                        }
                    }
                }
            ]
        },
        {
            fieldLabel: 'Geometrie (EPSG:4326)',
            name: 'geom',
            grow: true,
            anchor: '100%',
            editable: false,
            xtype: 'textareafield',
            allowBlank: true
        },
        {
            xtype: 'button',
            text: 'Bewerk geometrie op kaart',
            handler: function() {
                console.log('using new code');
                var panel, form, ident
                panel = this.up('panel');
                form = panel.getForm();
                ident = Lizard.CM.getContext().object.id;
                // Get the extent for the current object via
                // Request. Succes will open the editor
                Ext.Ajax.request({
                    url: '/area/api/area_special/'+ ident +'/',
                    method: 'GET',
                    params: {
                        _accept: 'application/json'
                    },
                    success: function(xhr) {
                        var extent
                        extent = Ext.JSON.decode(
                          xhr.responseText
                        ).area.extent;
                        Lizard.window.MapWindow.show({
                          callback: function(geometry) {
                            var form
                            form = panel.getForm();
                            form.findField('geom').setValue(geometry);
                          },
                          start_geometry: form.findField('geom').getValue(),
                          start_extent: extent
                        })
                    },
                    failure: function() {
                        Ext.Msg.alert(
                          "portal creation failed",
                          "Server communication failure"
                        );
                    }
                })
            }
        }
    ],
    buttons:[
    {
        text: 'Annuleren',
        handler: function() {
            this.up('window').close();
        }
    },{
        text: 'Opslaan',
        //formBind: true, //only enabled once the form is valid
        //disabled: true,
        handler: function() {
            var form = this.up('form').getForm();
            var form_window = this.up('window')
            if (form.isValid()) {
                /* todo: de waarden zelf gaan rangschikken en verzenden */
                var values = form.getValues()
                Lizard.window.EditSummaryBox.show({

                    fn: function (btn, text) {
                        if (btn=='ok') {
                            values.edit_summary = text;
                            form_window.setLoading(true);
                            Ext.Ajax.request({
                                url: '/annotation/api/annotationform/?action={% if annotation %}update{% else %}create{% endif %}&_accept=application/json&flat=false',
                                params: {
                                    object_id: values.id,
                                    edit_message: text,
                                    data:  Ext.JSON.encode(values)
                                },
                                method: 'POST',
                                callback: function(xhr) {
                                    Ext.Msg.alert("Opgeslagen", "Opslaan gelukt");
                                    form_window.close();
                                    form_window.setLoading(false);
                                    if (form_window.finish_edit_function) {
                                        form_window.finish_edit_function({% if annotation %}'update'{% else %}'create'{% endif%});
                                    } else {
                                        var store = Ext.StoreManager.lookup('analyse_store');
                                        store.load({params: {object_ident: Lizard.CM.getContext().object.id}});
                                        Ext.WindowManager.each(function(window) {
                                            if (window.loader) {
                                                window.loader.load();
                                            }
                                        })
                                    }
                                },
                                failure: function(xhr) {
                                    Ext.Msg.alert("Fout", "Server error");
                                    form_window.setLoading(false);
                                }
                            });

                        }
                        return true;
                    }
                })
            }
        }
    }]
}
