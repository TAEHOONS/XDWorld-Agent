---
description: 지도 내 평면 객체에 적용 될 스타일 옵션 설정하기 위한 API 입니다.
---

# JSPolygonStyle

> Module.JSPolygonStyle() API를 생성합니다.
>
> JSPolygonStyle을 통해 다양한 평면 객체 스타일의 일괄 설정이 가능합니다.

```javascript
var objectStyle = new Module.JSPolygonStyle();
```

## Getter / Setter

### getFill(), setFill(fill) → boolean

> 평면 객체의 채움 색상을 가시화 유무를 설정합니다.
>
> 기본적으로 true 옵션으로 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                               |
| ---- | ------- | --------------------------------------------------------- |
| fill | boolean | <p>true: 색상 가시화.<br>false: 평면 객체 옵션 가시화.<p> |

-   Return
    -   true: 색상 적용.
    -   false: 색상 미적용.

{% endtab %}
{% tab title="Template" %}

```javascript
var bOutlineUsed = polygon.getStyle().getFill();
// ... or ...
var figure = new Module.JSFigure();
// ...
var polyStyle = figure.getStyle();
polyStyle.setFill(true);
```

{% endtab %}
{% endtabs %}

### getFillColor(), setFillColor(color) → [JSColor](../core/jscolor.md)

> 평면 객체의 채움 색상을 설정합니다.

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
var figure = new Module.JSFigure();
//...
var polyStyle = figure.getStyle();
var fillColor = polyStyle.getFillColor();
// ... or ...
var polyStyle = figure.getStyle();
var fillColor = new Module.JSColor(255, 255, 100, 0);
polyStyle.setFillColor(fillColor);
```

{% endtab %}
{% endtabs %}

### getOutLine(), setOutLine(set) → boolean

> 평면 객체의 외곽선 가시화 유무를 설정합니다.
>
> 기본적으로 true 옵션으로 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| ---- | ------- | ------------------------------------------------------ |
| set  | boolean | <p>true: 외곽선 가시화.<br>false: 외곽선 비가시화.</p> |

-   Return
    -   true: 외곽선 적용.
    -   false: 외곽선 미적용.

{% endtab %}
{% tab title="Template" %}

```javascript
var outLineWidth = polygon.getStyle().getOutLineWidth();
// ... or ...
var figure = new Module.JSFigure();
//...
var polyStyle = figure.getStyle();
polyStyle.setOutLineWidth(5.0);
```

{% endtab %}
{% endtabs %}

### getOutLineWidth(), setOutLineWidth(lineWidth) → void

> 평면 객체의 외곽선 두께를 설정 및 반환합니다.
>
> 기본적으로 1.0 으로 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description |
| --------- | ------ | ----------- |
| lineWidth | number | 외곽선 두께   |

{% endtab %}
{% tab title="Template" %}

```javascript
var bOutlineUsed = polygon.getStyle().getOutLine();
// ... or ...
var figure = new Module.JSFigure();
//...
var polyStyle = figure.getStyle();
polyStyle.setOutLine(false);
```

{% endtab %}
{% endtabs %}

### getOutLineColor(), setOutLineColor(color) → [JSColor](../core/jscolor.md)

> 평면 객체의 외곽선 색상을 설정합니다.

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
var figure = new Module.JSFigure();
//...
var polyStyle = figure.getStyle();
var outlineColor = polyStyle.getOutLineColor();
// ... or ...
var figure = new Module.JSFigure();
//...
var polyStyle = figure.getStyle();
var outlineColor = new Module.JSColor(255, 255, 0, 0);
polyStyle.setOutLineColor(outlineColor);
```

{% endtab %}
{% endtabs %}
