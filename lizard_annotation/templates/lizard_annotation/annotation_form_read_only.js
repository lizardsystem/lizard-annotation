{
    xtype: 'formautoload',
    layout: 'anchor',
    autoScroll: true,
    trackResetOnLoad: true,
    bodyPadding: '10 25 10 10',//padding on the right side 25 for scrollbar
    height: '100%',
    loadProxy: {
        url: '/history/api_object/{{view.log_entry_id}}',
        type: 'ajax',
        method: 'GET',
        reader: {
          root: 'data',
          type: 'json'
        },
        params: {
            _accept: 'application/json',
        },
        success: function(form, action) {
            console.log('success gives:');
            console.log(arguments);
        },
        failure: function(form, action) {
            Ext.Msg.alert("Load failed", action.result.errorMessage);
        }
    },
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
                data: 'annotion_category'
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
                data: 'annotation_statuses'
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
        }
    ],
}
