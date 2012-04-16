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
            fieldLabel: 'Naam',
            name: 'title',
            width: 200,
            xtype: 'textfield',
            allowBlank: false
        },
        {
            fieldLabel: 'Datum aanvang periode',
            name: 'datetime_period_start',
            width: 200,
            xtype: 'datefield',
            allowBlank: true,
            format: 'd-m-Y',
            altFormats: 'Y-m-d h:m:s',
            submitFormat: 'Y-m-d h:m:s'
        },
        {
            fieldLabel: 'Datum einde periode',
            name: 'datetime_period_end',
            width: 200,
            xtype: 'datefield',
            allowBlank: true,
            format: 'd-m-Y',
            altFormats: 'Y-m-d h:m:s',
            submitFormat: 'Y-m-d h:m:s'
        },
        {
            fieldLabel: 'Omschrijving',
            name: 'description',
            anchor: '100%',
            xtype: 'htmleditor',
            allowBlank: false
        },
        {
            fieldLabel: 'Type',
            name: 'annotation_type',
            displayField: 'name',
            valueField: 'id',
            width: 400,
            xtype: 'combodict',
            store: {
                fields: ['id', 'name'],
                data: Ext.JSON.decode(
                  {% autoescape off %}
                  '{{ annotation_types }}'
                  {% endautoescape %})
            },
            multiSelect: false,
            forceSelection: true,
            allowBlank: false
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
            fieldLabel: 'Annotatie status',
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
                            url: '/area/api/catchment-areas/?node=root&_accept=application%2Fjson&size=id_name',
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
            text: 'edit geometry op kaart',
            handler: function() {
                panel = this.up('panel')
                form = panel.getForm()
                Lizard.window.MapWindow.show({
                    callback: function(geometry) {
                        form = panel.getForm();
                        form.findField('geom').setValue(geometry);
                    },
                    start_geometry: form.findField('geom').getValue()
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
                                success: function(xhr) {
                                    Ext.Msg.alert("Opgeslagen", "Opslaan gelukt");
                                    form_window.close();
                                    form_window.setLoading(false);
                                    if (form_window.finish_edit_function) {
                                        form_window.finish_edit_function({% if annotation %}'update'{% else %}'create'{% endif%});
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
