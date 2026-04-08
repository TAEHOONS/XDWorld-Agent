---
description: 지도 내 지형의 경사 분석 기능 설정을 위한 API입니다.
---

# JSSlope

> Module.getSlope API를 생성합니다.

```javascript
var Slope = Module.getSlope();
```

## Function

### clearAnalysisData()

> 분석 결과를 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getSlope().clearAnalysisData();
```

{% endtab %}
{% endtabs %}

### clearColorList() → boolean

> 분석 결과에 해당되는 범례 색상 목록을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true : 초기화 성공.
    -   false : 초기화 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getSlope().clearColorList();
```

{% endtab %}
{% endtabs %}

### getColorArea(key, index) → number

> 각 범례 인덱스 별 면적 값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                      |
| :---- | :----- | :------------------------------- |
| key   | string | 분석 결과 가시화 객체 고유 명칭. |
| index | number | 면적 값을 반환할 인덱스.         |

-   Return
    -   number(0 ~) : 범례에 해당하는 면적 반환 성공 (square meters 단위).
    -   -1 : index가 유효하지 않거나, key에 해당하는 오브젝트를 찾지 못한 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}
