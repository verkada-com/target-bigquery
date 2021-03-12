

"""
this schema is from here: https://bitbucket.org/analyticspros/dt-singerio-shopify/commits/

it has three instances of this:


,
                    {
                      "properties": {},
                      "type": [
                        "null",
                        "object"
                      ]
                    }
it's breaking the pipeline, if it's branch feature/schema-translation

it's running fine if it's master branch
"""


shopify_orders_malformed = """{"type":"SCHEMA",
      "stream": "orders",
      "tap_stream_id": "orders",
      "schema": {
        "properties": {
          "presentment_currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "subtotal_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_discounts_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_line_items_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_shipping_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_tax_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "line_items": {
            "items": {
              "properties": {
                "applied_discounts": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "properties": {
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "savings": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  }
                },
                "total_discount_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "pre_tax_price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "grams": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "compare_at_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "destination_location_id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "line_price": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "origin_location_id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "applied_discount": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "fulfillable_quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "variant_title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "properties": {
                  "anyOf": [
                    {
                      "items": {
                        "properties": {
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "value": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "type": [
                        "null",
                        "array"
                      ]
                    },
                    {
                      "properties": {},
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  ]
                },
                "tax_code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discount_allocations": {
                  "items": {
                    "properties": {
                      "discount_application_index": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "amount_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                          "type": [
                              "null",
                              "object"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "pre_tax_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "sku": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "product_exists": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "total_discount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "fulfillment_status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "gift_card": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "taxable": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "vendor": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "origin_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "requires_shipping": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "fulfillment_service": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_inventory_management": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "destination_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "product_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "processing_method": {
            "type": [
              "null",
              "string"
            ]
          },
          "order_number": {
            "type": [
              "null",
              "string"
            ]
          },
          "confirmed": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "total_discounts": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "total_line_items_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "order_adjustments": {
            "items": {
              "properties": {
                "order_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "refund_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "kind": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "reason": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "shipping_lines": {
            "items": {
              "properties": {
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "phone": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discounted_price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discount_allocations": {
                  "items": {
                    "properties": {
                      "discount_application_index": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "delivery_category": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discounted_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "requested_fulfillment_service_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "carrier_identifier": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "admin_graphql_api_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "device_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "cancel_reason": {
            "type": [
              "null",
              "string"
            ]
          },
          "currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "payment_gateway_names": {
            "items": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "source_identifier": {
            "type": [
              "null",
              "string"
            ]
          },
          "id": {
            "type": [
              "null",
              "string"
            ]
          },
          "processed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "referring_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "contact_email": {
            "type": [
              "null",
              "string"
            ]
          },
          "location_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "fulfillments": {
            "items": {
              "properties": {
                "location_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "receipt": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "properties": {
                    "testcase": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "authorization": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "tracking_number": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "created_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "shipment_status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "line_items": {
                  "items": {
                    "properties": {
                      "applied_discounts": {
                        "type": [
                          "null",
                          "array"
                        ],
                        "items": {
                          "properties": {
                            "title": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "code": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "amount": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "savings": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "type": {
                              "type": [
                                "null",
                                "string"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        }
                      },
                      "total_discount_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "pre_tax_price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "grams": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "compare_at_price": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "destination_location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "key": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "line_price": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "origin_location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "applied_discount": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "fulfillable_quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "variant_title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "properties": {
                        "anyOf": [
                          {
                            "items": {
                              "properties": {
                                "name": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "value": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          },
                          {
                            "properties": {},
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        ]
                      },
                      "tax_code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "discount_allocations": {
                        "items": {
                          "properties": {
                            "discount_application_index": {
                              "type": [
                                "null",
                                "integer"
                              ]
                            },
                            "amount_set": {
                              "properties": {
                                "shop_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "presentment_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                }
                              },
                                "type": [
                                    "null",
                                    "object"
                              ]
                            },
                            "amount": {
                              "type": [
                                "null",
                                "number"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        },
                        "type": [
                          "null",
                          "array"
                        ]
                      },
                      "admin_graphql_api_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "pre_tax_price": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "sku": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "product_exists": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "total_discount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "name": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "fulfillment_status": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "gift_card": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "taxable": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "vendor": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "tax_lines": {
                        "items": {
                          "properties": {
                            "price_set": {
                              "properties": {
                                "shop_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "presentment_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "price": {
                              "type": [
                                "null",
                                "number"
                              ],
                              "multipleOf": 1e-10
                            },
                            "title": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "rate": {
                              "type": [
                                "null",
                                "number"
                              ],
                              "multipleOf": 1e-10
                            },
                            "compare_at": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "position": {
                              "type": [
                                "null",
                                "integer"
                              ]
                            },
                            "source": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "zone": {
                              "type": [
                                "null",
                                "string"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        },
                        "type": [
                          "null",
                          "array"
                        ]
                      },
                      "origin_location": {
                        "properties": {
                          "country_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address1": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "city": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address2": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "province_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "zip": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "requires_shipping": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "fulfillment_service": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "variant_inventory_management": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "destination_location": {
                        "properties": {
                          "country_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address1": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "city": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address2": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "province_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "zip": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "product_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "variant_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "tracking_url": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "service": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tracking_urls": {
                  "items": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "tracking_numbers": {
                  "items": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tracking_company": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "updated_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "customer": {
            "type": "object",
            "properties": {
              "last_order_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "currency": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "email": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "multipass_identifier": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "default_address": {
                "type": [
                  "null",
                  "object"
                ],
                "properties": {
                  "city": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address1": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "zip": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "phone": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "first_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "customer_id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "default": {
                    "type": [
                      "null",
                      "boolean"
                    ]
                  },
                  "last_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address2": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "company": {
                    "type": [
                      "null",
                      "string"
                    ]
                  }
                }
              },
              "orders_count": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "state": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "verified_email": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "total_spent": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_order_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "updated_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "note": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "admin_graphql_api_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "addresses": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "properties": {
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "phone": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "first_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "customer_id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "default": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "last_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "company": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tags": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tax_exempt": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "accepts_marketing": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "accepts_marketing_updated_at": {
                "type": [
                    "string",
                    "null"
                ],
                "format": "date-time"
              },
              "created_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              }
            }
          },
          "test": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "total_tax": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "payment_details": {
            "properties": {
              "avs_result_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "cvv_result_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_bin": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_number": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "number": {
            "type": [
              "null",
              "integer"
            ]
          },
          "email": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_name": {
            "type": [
              "null",
              "string"
            ]
          },
          "landing_site_ref": {
            "type": [
              "null",
              "string"
            ]
          },
          "shipping_address": {
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price_usd": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "closed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "discount_applications": {
            "items": {
              "properties": {
                "target_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "description": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "target_selection": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "allocation_method": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "number"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "note": {
            "type": [
              "null",
              "string"
            ]
          },
          "user_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "subtotal_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "billing_address": {
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "landing_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "taxes_included": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "token": {
            "type": [
              "null",
              "string"
            ]
          },
          "app_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_tip_received": {
            "type": [
              "null",
              "number"
            ]
          },
          "browser_ip": {
            "type": [
              "null",
              "string"
            ]
          },
          "discount_codes": {
            "items": {
              "properties": {
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "tax_lines": {
            "items": {
              "properties": {
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "rate": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "compare_at": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "position": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "zone": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "phone": {
            "type": [
              "null",
              "string"
            ]
          },
          "note_attributes": {
            "items": {
              "properties": {
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "fulfillment_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "order_status_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "client_details": {
            "properties": {
              "session_hash": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "accept_language": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_width": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "user_agent": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_ip": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_height": {
                "type": [
                  "null",
                  "integer"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "buyer_accepts_marketing": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "checkout_token": {
            "type": [
              "null",
              "string"
            ]
          },
          "tags": {
            "type": [
              "null",
              "string"
            ]
          },
          "financial_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "customer_locale": {
            "type": [
              "null",
              "string"
            ]
          },
          "checkout_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_weight": {
            "type": [
              "null",
              "integer"
            ]
          },
          "gateway": {
            "type": [
              "null",
              "string"
            ]
          },
          "cart_token": {
            "type": [
              "null",
              "string"
            ]
          },
          "cancelled_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "refunds": {
            "items": {
              "properties": {
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "refund_line_items": {
                  "items": {
                    "properties": {
                      "line_item": {
                        "properties": {
                          "applied_discounts": {
                            "type": [
                              "null",
                              "array"
                            ],
                            "items": {
                              "properties": {
                                "title": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "code": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "amount": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "savings": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "type": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            }
                          },
                          "total_discount_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "pre_tax_price_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "price_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "grams": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "compare_at_price": {
                            "type": [
                              "null",
                              "number"
                            ]
                          },
                          "destination_location_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "key": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "line_price": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "origin_location_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "applied_discount": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "fulfillable_quantity": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "variant_title": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "properties": {
                            "anyOf": [
                              {
                                "items": {
                                  "properties": {
                                    "name": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "value": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "type": [
                                  "null",
                                  "array"
                                ]
                              },
                              {
                                "properties": {},
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            ]
                          },
                          "tax_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "discount_allocations": {
                            "items": {
                              "properties": {
                                "discount_application_index": {
                                  "type": [
                                    "null",
                                    "integer"
                                  ]
                                },
                                "amount_set": {
                                  "properties": {
                                    "shop_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    },
                                    "presentment_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    }
                                  },
                                    "type": [
                                        "null",
                                        "object"
                                  ]
                                },
                                "amount": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          },
                          "admin_graphql_api_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "pre_tax_price": {
                            "type": [
                              "null",
                              "number"
                            ]
                          },
                          "sku": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "product_exists": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "total_discount": {
                            "type": [
                              "null",
                              "number"
                            ],
                            "multipleOf": 1e-10
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "fulfillment_status": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "gift_card": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "taxable": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "vendor": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "tax_lines": {
                            "items": {
                              "properties": {
                                "price_set": {
                                  "properties": {
                                    "shop_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    },
                                    "presentment_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "price": {
                                  "type": [
                                    "null",
                                    "number"
                                  ],
                                  "multipleOf": 1e-10
                                },
                                "title": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "rate": {
                                  "type": [
                                    "null",
                                    "number"
                                  ],
                                  "multipleOf": 1e-10
                                },
                                "compare_at": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "position": {
                                  "type": [
                                    "null",
                                    "integer"
                                  ]
                                },
                                "source": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "zone": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          },
                          "origin_location": {
                            "properties": {
                              "country_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "name": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address1": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "city": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "id": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address2": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "province_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "zip": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "price": {
                            "type": [
                              "null",
                              "number"
                            ],
                            "multipleOf": 1e-10
                          },
                          "requires_shipping": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "fulfillment_service": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "variant_inventory_management": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "title": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "destination_location": {
                            "properties": {
                              "country_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "name": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address1": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "city": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "id": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address2": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "province_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "zip": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "quantity": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "product_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "variant_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "line_item_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "total_tax": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "restock_type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "subtotal": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "restock": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "note": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "user_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "created_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "processed_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "order_adjustments": {
                  "items": {
                    "properties": {
                      "order_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "tax_amount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "refund_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "kind": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "reason": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "updated_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "reference": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "id"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "updated_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "presentment_currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "subtotal_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_discounts_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_line_items_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_shipping_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tax_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "line_items"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "processing_method"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_number"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "confirmed"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_discounts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_line_items_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_adjustments"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "admin_graphql_api_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "device_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cancel_reason"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "payment_gateway_names"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_identifier"
          ],
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
            "processed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "referring_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "contact_email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "location_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "fulfillments"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "test"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tax"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "payment_details"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "number"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "landing_site_ref"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price_usd"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "closed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "discount_applications"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "user_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "subtotal_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "billing_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "landing_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "taxes_included"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "app_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tip_received"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "browser_ip"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "discount_codes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tax_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "phone"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note_attributes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "fulfillment_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_status_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "client_details"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "buyer_accepts_marketing"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "checkout_token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tags"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "financial_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer_locale"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "checkout_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_weight"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gateway"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cart_token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cancelled_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "refunds"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "updated_at"
          ],
          "metadata": {
            "inclusion": "automatic"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "reference"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "id"
      ],
      "replication_key": "updated_at",
      "replication_method": "INCREMENTAL"
    }"""

# removed the object/dict with emppty properties
shopify_orders_fixed = """
{"type":"SCHEMA",
      "stream": "orders",
      "tap_stream_id": "orders",
      "schema": {
        "properties": {
          "presentment_currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "subtotal_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_discounts_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_line_items_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_shipping_price_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_tax_set": {
            "properties": {
              "shop_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              },
              "presentment_money": {
                "properties": {
                  "currency_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                },
                "type": [
                  "null",
                  "object"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "line_items": {
            "items": {
              "properties": {
                "applied_discounts": {
                  "type": [
                    "null",
                    "array"
                  ],
                  "items": {
                    "properties": {
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "savings": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  }
                },
                "total_discount_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "pre_tax_price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "grams": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "compare_at_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "destination_location_id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "line_price": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "origin_location_id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "applied_discount": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "fulfillable_quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "variant_title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "properties": {
                  "anyOf": [
                    {
                      "items": {
                        "properties": {
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "value": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "type": [
                        "null",
                        "array"
                      ]
                    }
                  ]
                },
                "tax_code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discount_allocations": {
                  "items": {
                    "properties": {
                      "discount_application_index": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "amount_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                          "type": [
                              "null",
                              "object"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "pre_tax_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "sku": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "product_exists": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "total_discount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "fulfillment_status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "gift_card": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "taxable": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "vendor": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "origin_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "requires_shipping": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "fulfillment_service": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_inventory_management": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "destination_location": {
                  "properties": {
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "quantity": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "product_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "variant_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "processing_method": {
            "type": [
              "null",
              "string"
            ]
          },
          "order_number": {
            "type": [
              "null",
              "string"
            ]
          },
          "confirmed": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "total_discounts": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "total_line_items_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "order_adjustments": {
            "items": {
              "properties": {
                "order_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tax_amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "refund_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "kind": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "reason": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "shipping_lines": {
            "items": {
              "properties": {
                "tax_lines": {
                  "items": {
                    "properties": {
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "rate": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "compare_at": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "position": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "source": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "zone": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "phone": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discounted_price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discount_allocations": {
                  "items": {
                    "properties": {
                      "discount_application_index": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "delivery_category": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "discounted_price": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "requested_fulfillment_service_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "carrier_identifier": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "admin_graphql_api_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "device_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "cancel_reason": {
            "type": [
              "null",
              "string"
            ]
          },
          "currency": {
            "type": [
              "null",
              "string"
            ]
          },
          "payment_gateway_names": {
            "items": {
              "type": [
                "null",
                "string"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "source_identifier": {
            "type": [
              "null",
              "string"
            ]
          },
          "id": {
            "type": [
              "null",
              "string"
            ]
          },
          "processed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "referring_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "contact_email": {
            "type": [
              "null",
              "string"
            ]
          },
          "location_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "fulfillments": {
            "items": {
              "properties": {
                "location_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "receipt": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "properties": {
                    "testcase": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "authorization": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                "tracking_number": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "created_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "shipment_status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "line_items": {
                  "items": {
                    "properties": {
                      "applied_discounts": {
                        "type": [
                          "null",
                          "array"
                        ],
                        "items": {
                          "properties": {
                            "title": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "code": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "amount": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "savings": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "type": {
                              "type": [
                                "null",
                                "string"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        }
                      },
                      "total_discount_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "pre_tax_price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price_set": {
                        "properties": {
                          "shop_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "presentment_money": {
                            "properties": {
                              "currency_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "amount": {
                                "type": [
                                  "null",
                                  "number"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "grams": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "compare_at_price": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "destination_location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "key": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "line_price": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "origin_location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "applied_discount": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "fulfillable_quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "variant_title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "properties": {
                        "anyOf": [
                          {
                            "items": {
                              "properties": {
                                "name": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "value": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          }
                        ]
                      },
                      "tax_code": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "discount_allocations": {
                        "items": {
                          "properties": {
                            "discount_application_index": {
                              "type": [
                                "null",
                                "integer"
                              ]
                            },
                            "amount_set": {
                              "properties": {
                                "shop_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "presentment_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                }
                              },
                                "type": [
                                    "null",
                                    "object"
                              ]
                            },
                            "amount": {
                              "type": [
                                "null",
                                "number"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        },
                        "type": [
                          "null",
                          "array"
                        ]
                      },
                      "admin_graphql_api_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "pre_tax_price": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "sku": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "product_exists": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "total_discount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "name": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "fulfillment_status": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "gift_card": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "taxable": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "vendor": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "tax_lines": {
                        "items": {
                          "properties": {
                            "price_set": {
                              "properties": {
                                "shop_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "presentment_money": {
                                  "properties": {
                                    "currency_code": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "amount": {
                                      "type": [
                                        "null",
                                        "number"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "price": {
                              "type": [
                                "null",
                                "number"
                              ],
                              "multipleOf": 1e-10
                            },
                            "title": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "rate": {
                              "type": [
                                "null",
                                "number"
                              ],
                              "multipleOf": 1e-10
                            },
                            "compare_at": {
                              "type": [
                                "null",
                                "number"
                              ]
                            },
                            "position": {
                              "type": [
                                "null",
                                "integer"
                              ]
                            },
                            "source": {
                              "type": [
                                "null",
                                "string"
                              ]
                            },
                            "zone": {
                              "type": [
                                "null",
                                "string"
                              ]
                            }
                          },
                          "type": [
                            "null",
                            "object"
                          ]
                        },
                        "type": [
                          "null",
                          "array"
                        ]
                      },
                      "origin_location": {
                        "properties": {
                          "country_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address1": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "city": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address2": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "province_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "zip": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "price": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "requires_shipping": {
                        "type": [
                          "null",
                          "boolean"
                        ]
                      },
                      "fulfillment_service": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "variant_inventory_management": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "title": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "destination_location": {
                        "properties": {
                          "country_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address1": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "city": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "address2": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "province_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "zip": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "product_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "variant_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "tracking_url": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "service": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "status": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tracking_urls": {
                  "items": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "tracking_numbers": {
                  "items": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "tracking_company": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "updated_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "customer": {
            "type": "object",
            "properties": {
              "last_order_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "currency": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "email": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "multipass_identifier": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "default_address": {
                "type": [
                  "null",
                  "object"
                ],
                "properties": {
                  "city": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address1": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "zip": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "phone": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "first_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "customer_id": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "default": {
                    "type": [
                      "null",
                      "boolean"
                    ]
                  },
                  "last_name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "country_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "name": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "province_code": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "address2": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "company": {
                    "type": [
                      "null",
                      "string"
                    ]
                  }
                }
              },
              "orders_count": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "state": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "verified_email": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "total_spent": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_order_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "updated_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              },
              "note": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "admin_graphql_api_id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "addresses": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "properties": {
                    "city": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address1": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "zip": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "phone": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "first_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "customer_id": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "default": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "last_name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "country_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "province_code": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "address2": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "company": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tags": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "tax_exempt": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "id": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "accepts_marketing": {
                "type": [
                  "null",
                  "boolean"
                ]
              },
              "accepts_marketing_updated_at": {
                "type": [
                    "string",
                    "null"
                ],
                "format": "date-time"
              },
              "created_at": {
                "type": [
                  "null",
                  "string"
                ],
                "format": "date-time"
              }
            }
          },
          "test": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "total_tax": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "payment_details": {
            "properties": {
              "avs_result_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "cvv_result_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_bin": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "credit_card_number": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "number": {
            "type": [
              "null",
              "integer"
            ]
          },
          "email": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_name": {
            "type": [
              "null",
              "string"
            ]
          },
          "landing_site_ref": {
            "type": [
              "null",
              "string"
            ]
          },
          "shipping_address": {
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "total_price_usd": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "closed_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "discount_applications": {
            "items": {
              "properties": {
                "target_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "description": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "target_selection": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "allocation_method": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value_type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "number"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "name": {
            "type": [
              "null",
              "string"
            ]
          },
          "note": {
            "type": [
              "null",
              "string"
            ]
          },
          "user_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "source_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "subtotal_price": {
            "type": [
              "null",
              "number"
            ],
            "multipleOf": 1e-10
          },
          "billing_address": {
            "properties": {
              "phone": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "country": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "address1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "longitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "address2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "last_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "first_name": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "city": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "company": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "latitude": {
                "type": [
                  "null",
                  "number"
                ]
              },
              "country_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "province_code": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "zip": {
                "type": [
                  "null",
                  "string"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "landing_site": {
            "type": [
              "null",
              "string"
            ]
          },
          "taxes_included": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "token": {
            "type": [
              "null",
              "string"
            ]
          },
          "app_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_tip_received": {
            "type": [
              "null",
              "number"
            ]
          },
          "browser_ip": {
            "type": [
              "null",
              "string"
            ]
          },
          "discount_codes": {
            "items": {
              "properties": {
                "code": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "amount": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "tax_lines": {
            "items": {
              "properties": {
                "price_set": {
                  "properties": {
                    "shop_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    },
                    "presentment_money": {
                      "properties": {
                        "currency_code": {
                          "type": [
                            "null",
                            "string"
                          ]
                        },
                        "amount": {
                          "type": [
                            "null",
                            "number"
                          ]
                        }
                      },
                      "type": [
                        "null",
                        "object"
                      ]
                    }
                  },
                  "type": [
                    "null",
                    "object"
                  ]
                },
                "price": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "title": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "rate": {
                  "type": [
                    "null",
                    "number"
                  ],
                  "multipleOf": 1e-10
                },
                "compare_at": {
                  "type": [
                    "null",
                    "number"
                  ]
                },
                "position": {
                  "type": [
                    "null",
                    "integer"
                  ]
                },
                "source": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "zone": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "phone": {
            "type": [
              "null",
              "string"
            ]
          },
          "note_attributes": {
            "items": {
              "properties": {
                "name": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "fulfillment_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "order_status_url": {
            "type": [
              "null",
              "string"
            ]
          },
          "client_details": {
            "properties": {
              "session_hash": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "accept_language": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_width": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "user_agent": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_ip": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "browser_height": {
                "type": [
                  "null",
                  "integer"
                ]
              }
            },
            "type": [
              "null",
              "object"
            ]
          },
          "buyer_accepts_marketing": {
            "type": [
              "null",
              "boolean"
            ]
          },
          "checkout_token": {
            "type": [
              "null",
              "string"
            ]
          },
          "tags": {
            "type": [
              "null",
              "string"
            ]
          },
          "financial_status": {
            "type": [
              "null",
              "string"
            ]
          },
          "customer_locale": {
            "type": [
              "null",
              "string"
            ]
          },
          "checkout_id": {
            "type": [
              "null",
              "string"
            ]
          },
          "total_weight": {
            "type": [
              "null",
              "integer"
            ]
          },
          "gateway": {
            "type": [
              "null",
              "string"
            ]
          },
          "cart_token": {
            "type": [
              "null",
              "string"
            ]
          },
          "cancelled_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "refunds": {
            "items": {
              "properties": {
                "admin_graphql_api_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "refund_line_items": {
                  "items": {
                    "properties": {
                      "line_item": {
                        "properties": {
                          "applied_discounts": {
                            "type": [
                              "null",
                              "array"
                            ],
                            "items": {
                              "properties": {
                                "title": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "code": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "amount": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "savings": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "type": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            }
                          },
                          "total_discount_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "pre_tax_price_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "price_set": {
                            "properties": {
                              "shop_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              },
                              "presentment_money": {
                                "properties": {
                                  "currency_code": {
                                    "type": [
                                      "null",
                                      "string"
                                    ]
                                  },
                                  "amount": {
                                    "type": [
                                      "null",
                                      "number"
                                    ]
                                  }
                                },
                                "type": [
                                  "null",
                                  "object"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "grams": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "compare_at_price": {
                            "type": [
                              "null",
                              "number"
                            ]
                          },
                          "destination_location_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "key": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "line_price": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "origin_location_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "applied_discount": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "fulfillable_quantity": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "variant_title": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "properties": {
                            "anyOf": [
                              {
                                "items": {
                                  "properties": {
                                    "name": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    },
                                    "value": {
                                      "type": [
                                        "null",
                                        "string"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "type": [
                                  "null",
                                  "array"
                                ]
                              }
                            ]
                          },
                          "tax_code": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "discount_allocations": {
                            "items": {
                              "properties": {
                                "discount_application_index": {
                                  "type": [
                                    "null",
                                    "integer"
                                  ]
                                },
                                "amount_set": {
                                  "properties": {
                                    "shop_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    },
                                    "presentment_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    }
                                  },
                                    "type": [
                                        "null",
                                        "object"
                                  ]
                                },
                                "amount": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          },
                          "admin_graphql_api_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "pre_tax_price": {
                            "type": [
                              "null",
                              "number"
                            ]
                          },
                          "sku": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "product_exists": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "total_discount": {
                            "type": [
                              "null",
                              "number"
                            ],
                            "multipleOf": 1e-10
                          },
                          "name": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "fulfillment_status": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "gift_card": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "taxable": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "vendor": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "tax_lines": {
                            "items": {
                              "properties": {
                                "price_set": {
                                  "properties": {
                                    "shop_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    },
                                    "presentment_money": {
                                      "properties": {
                                        "currency_code": {
                                          "type": [
                                            "null",
                                            "string"
                                          ]
                                        },
                                        "amount": {
                                          "type": [
                                            "null",
                                            "number"
                                          ]
                                        }
                                      },
                                      "type": [
                                        "null",
                                        "object"
                                      ]
                                    }
                                  },
                                  "type": [
                                    "null",
                                    "object"
                                  ]
                                },
                                "price": {
                                  "type": [
                                    "null",
                                    "number"
                                  ],
                                  "multipleOf": 1e-10
                                },
                                "title": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "rate": {
                                  "type": [
                                    "null",
                                    "number"
                                  ],
                                  "multipleOf": 1e-10
                                },
                                "compare_at": {
                                  "type": [
                                    "null",
                                    "number"
                                  ]
                                },
                                "position": {
                                  "type": [
                                    "null",
                                    "integer"
                                  ]
                                },
                                "source": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                },
                                "zone": {
                                  "type": [
                                    "null",
                                    "string"
                                  ]
                                }
                              },
                              "type": [
                                "null",
                                "object"
                              ]
                            },
                            "type": [
                              "null",
                              "array"
                            ]
                          },
                          "origin_location": {
                            "properties": {
                              "country_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "name": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address1": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "city": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "id": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address2": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "province_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "zip": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "price": {
                            "type": [
                              "null",
                              "number"
                            ],
                            "multipleOf": 1e-10
                          },
                          "requires_shipping": {
                            "type": [
                              "null",
                              "boolean"
                            ]
                          },
                          "fulfillment_service": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "variant_inventory_management": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "title": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "destination_location": {
                            "properties": {
                              "country_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "name": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address1": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "city": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "id": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "address2": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "province_code": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "zip": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              }
                            },
                            "type": [
                              "null",
                              "object"
                            ]
                          },
                          "quantity": {
                            "type": [
                              "null",
                              "integer"
                            ]
                          },
                          "product_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          },
                          "variant_id": {
                            "type": [
                              "null",
                              "string"
                            ]
                          }
                        },
                        "type": [
                          "null",
                          "object"
                        ]
                      },
                      "location_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "line_item_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "quantity": {
                        "type": [
                          "null",
                          "integer"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "total_tax": {
                        "type": [
                          "null",
                          "number"
                        ]
                      },
                      "restock_type": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "subtotal": {
                        "type": [
                          "null",
                          "number"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                },
                "restock": {
                  "type": [
                    "null",
                    "boolean"
                  ]
                },
                "note": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "user_id": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "created_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "processed_at": {
                  "type": [
                    "null",
                    "string"
                  ],
                  "format": "date-time"
                },
                "order_adjustments": {
                  "items": {
                    "properties": {
                      "order_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "tax_amount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "refund_id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "amount": {
                        "type": [
                          "null",
                          "number"
                        ],
                        "multipleOf": 1e-10
                      },
                      "kind": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "id": {
                        "type": [
                          "null",
                          "string"
                        ]
                      },
                      "reason": {
                        "type": [
                          "null",
                          "string"
                        ]
                      }
                    },
                    "type": [
                      "null",
                      "object"
                    ]
                  },
                  "type": [
                    "null",
                    "array"
                  ]
                }
              },
              "type": [
                "null",
                "object"
              ]
            },
            "type": [
              "null",
              "array"
            ]
          },
          "created_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "updated_at": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "reference": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "type": "object"
      },
      "metadata": [
        {
          "breadcrumb": [],
          "metadata": {
            "table-key-properties": [
              "id"
            ],
            "forced-replication-method": "INCREMENTAL",
            "valid-replication-keys": [
              "updated_at"
            ],
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "presentment_currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "subtotal_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_discounts_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_line_items_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_shipping_price_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tax_set"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "line_items"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "processing_method"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_number"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "confirmed"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_discounts"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_line_items_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_adjustments"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "admin_graphql_api_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "device_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cancel_reason"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "currency"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "payment_gateway_names"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_identifier"
          ],
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
            "processed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "referring_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "contact_email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "location_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "fulfillments"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "test"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tax"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "payment_details"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "number"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "email"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "landing_site_ref"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "shipping_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_price_usd"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "closed_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "discount_applications"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "name"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "user_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "source_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "subtotal_price"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "billing_address"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "landing_site"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "taxes_included"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "app_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_tip_received"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "browser_ip"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "discount_codes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tax_lines"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "phone"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "note_attributes"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "fulfillment_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "order_status_url"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "client_details"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "buyer_accepts_marketing"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "checkout_token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "tags"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "financial_status"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "customer_locale"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "checkout_id"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "total_weight"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "gateway"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cart_token"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "cancelled_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "refunds"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "created_at"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        },
        {
          "breadcrumb": [
            "properties",
            "updated_at"
          ],
          "metadata": {
            "inclusion": "automatic"
          }
        },
        {
          "breadcrumb": [
            "properties",
            "reference"
          ],
          "metadata": {
            "inclusion": "available",
            "selected": true
          }
        }
      ],
      "key_properties": [
        "id"
      ],
      "replication_key": "updated_at",
      "replication_method": "INCREMENTAL"
    }
"""

