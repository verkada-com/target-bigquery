amazon_orders = """{
    "type": "SCHEMA",
    "tap_stream_id": "orders",
    "stream": "orders",
    "key_properties": [
        "id"
    ],
    "schema": {
        "type": "object",
        "properties": {
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "SellerOrderId": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "PurchaseDate": {
                "type": [
                    "null",
                    "string"
                ],
                "format": "date-time"
            },
            "LatestShipDate": {
                "type": [
                    "null",
                    "string"
                ],
                "format": "date-time"
            },
            "AmazonOrderId": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "OrderStatus": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "SalesChannel": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "IsBusinessOrder": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "IsPrime": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "BuyerName": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "BuyerEmail": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "FulfillmentChannel": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "IsPremiumOrder": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "IsReplacementOrder": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "LastUpdateDate": {
                "type": [
                    "null",
                    "string"
                ],
                "format": "date-time"
            },
            "MarketplaceId": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "NumberOfItemsUnshipped": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "NumberOfItemsShipped": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "OrderType": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "PaymentMethod": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "ShipServiceLevel": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "ShipServiceLevelCategory": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "OrderTotal": {
                "type": [
                    "null",
                    "object"
                ],
                "properties": {
                    "CurrencyCode": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "Amount": {
                        "type": [
                            "null",
                            "number"
                        ]
                    }
                }
            },
            "EarliestShipDate": {
                "type": [
                    "null",
                    "string"
                ],
                "format": "date-time"
            },
            "ShippingDiscount": {
                "type": [
                    "null",
                    "object"
                ],
                "properties": {
                    "CurrencyCode": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "Amount": {
                        "type": [
                            "null",
                            "number"
                        ]
                    }
                }
            },
            "PromotionDiscount": {
                "type": [
                    "null",
                    "object"
                ],
                "properties": {
                    "CurrencyCode": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "Amount": {
                        "type": [
                            "null",
                            "number"
                        ]
                    }
                }
            },
            "ShippingAddress": {
                "type": "object",
                "properties": {
                    "City": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "PostalCode": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "StateOrRegion": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "CountryCode": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "Name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "AddressLine1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "AddressLine2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
            },
            "OrderItems": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "QuantityOrdered": {
                            "type": [
                                "null",
                                "number"
                            ]
                        },
                        "Title": {
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        "IsGift": {
                            "type": [
                                "null",
                                "boolean"
                            ]
                        },
                        "ASIN": {
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        "SellerSKU": {
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        "OrderItemId": {
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        "CustomizedURL": {
                            "type": [
                                "null",
                                "string"
                            ]
                        },
                        "IsTransparency": {
                            "type": [
                                "null",
                                "boolean"
                            ]
                        },
                        "QuantityShipped": {
                            "type": [
                                "null",
                                "number"
                            ]
                        },
                        "ItemPrice": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "CurrencyCode": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "Amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                }
                            }
                        },
                        "ItemTax": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "CurrencyCode": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "Amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                }
                            }
                        },
                        "PromotionDiscount": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "CurrencyCode": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "Amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                }
                            }
                        },
                        "PromotionDiscountTax": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "CurrencyCode": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "Amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                }
                            }
                        },
                        "ProductInfo": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "NumberOfItems": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "SerialNumberRequired": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "SellerOrderId"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "PurchaseDate"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "LatestShipDate"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "AmazonOrderId"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "OrderStatus"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "SalesChannel"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "IsBusinessOrder"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "IsPrime"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "BuyerName"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "BuyerEmail"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "FulfillmentChannel"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "IsPremiumOrder"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "IsReplacementOrder"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "LastUpdateDate"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "MarketplaceId"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "NumberOfItemsUnshipped"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "NumberOfItemsShipped"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "OrderType"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "PaymentMethod"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "ShipServiceLevel"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "ShipServiceLevelCategory"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "OrderTotal"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "EarliestShipDate"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "ShippingDiscount"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "PromotionDiscount"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "ShippingAddress"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "OrderItems"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""
amazon_inventory = """{
    "type": "SCHEMA",
    "tap_stream_id": "inventory",
    "stream": "inventory",
    "key_properties": [
        "id"
    ],
    "schema": {
        "type": "object",
        "properties": {
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "ASIN": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "FNSKU": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "SellerSKU": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "Condition": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "TotalSupplyQuantity": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "InStockSupplyQuantity": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "EarliestAvailability": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "SupplyDetail": {
                "type": [
                    "null",
                    "object"
                ],
                "properties": {
                    "member": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "SupplyType": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "LatestAvailableToPick": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "properties": {
                                        "DateTime": {
                                            "type": [
                                                "null",
                                                "string"
                                            ],
                                            "format": "date-time"
                                        },
                                        "TimepointType": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                },
                                "Quantity": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "EarliestAvailableToPick": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "properties": {
                                        "DateTime": {
                                            "type": [
                                                "null",
                                                "string"
                                            ],
                                            "format": "date-time"
                                        },
                                        "TimepointType": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "ASIN"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "FNSKU"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "SellerSKU"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "Condition"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "SupplyDetail"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "TotalSupplyQuantity"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "InStockSupplyQuantity"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "EarliestAvailability"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""
amazon_products = """{
    "type": "SCHEMA",
    "tap_stream_id": "products",
    "stream": "products",
    "key_properties": [
        "id"
    ],
    "schema": {
        "type": "object",
        "properties": {
            "id": {
                "type": "string"
            },
            "IdType": {
                "type": "string"
            },
            "Product": {
                "type": ["null", "object"],
                "properties": {
                    "AttributeSets": {
                        "type": ["null", "object"],
                        "properties": {
                            "ItemAttributes": {
                                "type": ["null", "object"],
                                "properties": {
                                    "Binding": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Brand": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Flavor": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Label": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "ListPrice": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "number"]
                                            },
                                            "Amount": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "value": {
                                                        "type": [
                                                            "null",
                                                            "number"
                                                        ]
                                                    }
                                                }
                                            },
                                            "CurrencyCode": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "value": {
                                                        "type": ["null", "string"]
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "Manufacturer": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "ProductGroup": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "ProductTypeName": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Publisher": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Size": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Studio": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "Title": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "lang": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "PartNumber": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "value": {
                                                "type": ["null", "string"]
                                            }
                                        }
                                    },
                                    "ItemDimensions": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "Height": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            },
                                            "Width": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            },
                                            "Length": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "SmallImage": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "Height": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "integer"]
                                                    }
                                                }
                                            },
                                            "Width": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "integer"]
                                                    }
                                                }
                                            },
                                            "URL": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "value": {
                                                        "type": ["null", "string"]
                                                    }

                                                }

                                            }
                                        }
                                    },
                                    "PackageDimensions": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "Height": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            },
                                            "Width": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            },
                                            "Length": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            },
                                            "Weight": {
                                                "type": ["null", "object"],
                                                "properties": {
                                                    "Units": {
                                                        "type": ["null", "object"],
                                                        "properties": {
                                                            "value": {
                                                                "type": ["null", "string"]
                                                            }
                                                        }
                                                    },
                                                    "value": {
                                                        "type": ["null", "number"]
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }

                            }
                        }
                    },
                    "Identifiers": {
                        "type": ["null", "object"],
                        "properties": {
                            "MarketplaceASIN": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "ASIN": {
                                        "type": [
                                            "null",
                                            "object"
                                        ],
                                        "properties": {
                                            "value": {
                                                "type": [
                                                    "null",
                                                    "string"
                                                ]
                                            }
                                        }
                                    },
                                    "MarketplaceId": {
                                        "type": [
                                            "null",
                                            "object"
                                        ],
                                        "properties": {
                                            "value": {
                                                "type": [
                                                    "null",
                                                    "string"
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "Relationships": {
                        "type": ["null", "object"],
                        "properties": {
                            "VariationParent": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "Identifiers": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "MarketplaceASIN": {
                                                "type": [
                                                    "null",
                                                    "object"
                                                ],
                                                "properties": {
                                                    "ASIN": {
                                                        "type": [
                                                            "null",
                                                            "object"
                                                        ],
                                                        "properties": {
                                                            "value": {
                                                                "type": [
                                                                    "null",
                                                                    "string"
                                                                ]
                                                            }
                                                        }
                                                    },
                                                    "MarketplaceId": {
                                                        "type": [
                                                            "null",
                                                            "object"
                                                        ],
                                                        "properties": {
                                                            "value": {
                                                                "type": [
                                                                    "null",
                                                                    "string"
                                                                ]
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "VariationChild": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "Identifiers": {
                                        "type": ["null", "object"],
                                        "properties": {
                                            "MarketplaceASIN": {
                                                "type": [
                                                    "null",
                                                    "object"
                                                ],
                                                "properties": {
                                                    "ASIN": {
                                                        "type": [
                                                            "null",
                                                            "object"
                                                        ],
                                                        "properties": {
                                                            "value": {
                                                                "type": [
                                                                    "null",
                                                                    "string"
                                                                ]
                                                            }
                                                        }
                                                    },
                                                    "MarketplaceId": {
                                                        "type": [
                                                            "null",
                                                            "object"
                                                        ],
                                                        "properties": {
                                                            "value": {
                                                                "type": [
                                                                    "null",
                                                                    "string"
                                                                ]
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "SalesRankings": {
                        "type": ["null", "object"],
                        "properties": {
                            "SalesRank": {
                                "type": "array",
                                "items": {
                                    "type": ["null", "object"],
                                    "properties": {
                                        "ProductCategoryId": {
                                            "type": [
                                                "null",
                                                "object"
                                            ],
                                            "properties": {
                                                "value": {
                                                    "type": [
                                                        "null",
                                                        "string"
                                                    ]
                                                }
                                            }
                                        },
                                        "Rank": {
                                            "type": [
                                                "null",
                                                "object"
                                            ],
                                            "properties": {
                                                "value": {
                                                    "type": [
                                                        "null",
                                                        "string"
                                                    ]
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "IdType"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "Product"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]}"""