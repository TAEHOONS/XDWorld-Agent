---
description: 지도 내 직선 객체에 적용 될 스타일 옵션 설정하기 위한 API 입니다.
---

# JSPolyLineStyle

> Module.JSPolyLineStyle() API를 생성합니다.
>
> JSPolyLineStyle을 통해 다양한 직선 객체 스타일의 일괄 설정이 가능합니다.

```javascript
var objectStyle = new Module.JSPolyLineStyle();
```

## Getter / Setter

### getColor(), setColor(color) → [JSColor](../core/jscolor.md)

> 직선 객체의 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| color | [JSColor](../core/jscolor.md) | 색상값.     |

-   Return
    -   [JSColor](../core/jscolor.md): 적용 색상값.

{% endtab %}
{% tab title="Template" %}

```javascript
var color = polyline.getStyle().getColor();
// ... or ...
polyline.getStyle().setColor(new Module.JSColor(255, 255, 255, 255));
```

{% endtab %}
{% endtabs %}

### getWidth(), setWidth(width) → number

> 직선 객체의 두께를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| width | number | 두께.       |

-   Return
    -   number: 적용 두께.

{% endtab %}
{% tab title="Template" %}

```javascript
var width = polyline.getStyle().getWidth();
// ... or ...
polyline.getStyle().setWidth(10.0);
```

{% endtab %}
{% endtabs %}
